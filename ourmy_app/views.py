from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from ourmy_app.models import Campaign, Action, CampaignUser, UserAction, Prize
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib.sites.models import get_current_site
from django.template import loader
import datetime
import simplejson
from singly.singly import Singly
from urllib import urlencode
from ourmy_project.settings import SINGLY_CLIENT_ID, SINGLY_CLIENT_SECRET, SINGLY_REDIRECT_URI
from django.conf import settings
from django.core import serializers
from django.conf import settings
import bitly_api

from django import forms
from ourmy_app.forms import CampaignForm, PrizeForm
from django.utils.functional import LazyObject
import sharing
from sharing import get_points_for_user
from sharing.models import SharingCampaign, SharingCampaignUser, SharingAction, SharingUserAction
from annoying.functions import get_object_or_None


def index(request):
    current_campaign_list = Campaign.objects.filter(deadline__gt=datetime.datetime.now)
    # this is only a first-time setup thing (because we have no login)
    if len(Campaign.objects.all()) == 0:
        if request.user.is_authenticated():
            user = request.user
            campaign = Campaign(title="deleteme", user=user)
            campaign.save()
            fb_action = Action(campaign=campaign, title="facebook", api_call="sharing.get_facebook_post_actions_for_user")
            fb_action.save()
            tw_action = Action(campaign=campaign, title="twitter", api_call="sharing.get_twitter_post_actions_for_user")
            tw_action.save()
            fb_sharing_action = SharingAction(action=fb_action, social_network='FB', post_or_click=False)
            fb_sharing_action.save()
            tw_sharing_action = SharingAction(action=tw_action, social_network='TW', post_or_click=False)
            tw_sharing_action.save()
            current_campaign_list = Campaign.objects.filter(deadline__gt=datetime.datetime.now)
    return render_to_response('index.html', 
        {'campaign_list':current_campaign_list},
        context_instance=RequestContext(request))

@login_required
def create_campaign(request, campaign_id=None):
    campaign=None
    campaigns = []
    campaigns = Campaign.objects.filter(user=request.user)
    is_saved = False

    if request.method == 'POST':
        if campaign_id is not None:
            campaign = get_object_or_404(Campaign, pk=campaign_id)
            is_saved = True

        form = CampaignForm(request.POST, request.FILES, instance=campaign)
        if form.is_valid():
            form.instance.user = request.user
            # ZT001:  this is temporary -- when we can promote non-video urls we'll put it back into the form.
            form.instance.video_url = request.POST['long_url']
            form.save()

            sharing_campaign, created = SharingCampaign.objects.get_or_create(campaign=form.instance)
            sharing_campaign.long_url = request.POST['long_url']
            sharing_campaign.post_text = request.POST['post_text']
            sharing_campaign.save()
            # now we create the actions and sharing actions.  One post for each service, one click.
            services = SharingAction.SOCIAL_NETWORK_CHOICES
            for service in services:
                post_action, created = Action.objects.get_or_create(campaign=form.instance, title=service[1], points=10,
                                    api_call="sharing.get_%s_post_actions_for_user" % service[1])
                post_action.save()
                sharing_post_action, created = SharingAction.objects.get_or_create(action=post_action, social_network=service[0], post_or_click=False)
                sharing_post_action.save()
            click_action, created = Action.objects.get_or_create(campaign=form.instance, title="click", points=1,
                                  api_call="sharing.get_click_actions_for_user")
            click_action.save()
            sharing_click_action, created = SharingAction.objects.get_or_create(action=click_action, social_network=service[0], post_or_click=True)
            sharing_click_action.save()
            # return HttpResponseRedirect("/")
            url = reverse('edit_campaign', kwargs={'campaign_id':form.instance.id})
            return HttpResponseRedirect(url)
        else:
            print "printing form errors:"
            print form.errors
    else:
        if campaign_id is not None:
            campaign = get_object_or_404(Campaign, pk=campaign_id)
            is_saved = True
            sharing_campaign = SharingCampaign.objects.get(campaign=campaign)
            form = CampaignForm(instance=campaign, initial={'long_url':sharing_campaign.long_url, 'post_text':sharing_campaign.post_text})
        else:
            form = CampaignForm()

    return render_to_response("create_campaign.html", {'form':form, 'campaigns':campaigns, 'this_campaign':campaign, 'is_saved':is_saved},
        context_instance=RequestContext(request))

@login_required
def create_prize(request, prize_id=None, campaign_id=None):
    instance = None
    prizes_for_campaign = None
    campaign = None
    is_saved = False
    # we will either get a campaign_id (create) or a pitch_id (edit)
    # if there's a campaign id, this is a new prize.  Get the campaign, create & save the prize
    if campaign_id:
        campaign = get_object_or_404(Campaign, pk=campaign_id)
        prizes_for_campaign = Prize.objects.filter(campaign=campaign)
        instance = Prize(campaign=campaign)
    elif prize_id:
        instance = get_object_or_404(Prize, pk=prize_id)
        campaign = instance.campaign
        prizes_for_campaign = Prize.objects.filter(campaign=campaign)
        is_saved = True
    if request.method == 'POST':
        instance = get_object_or_None(Prize, campaign=campaign, title=request.POST['title'])
        if instance is None:
            instance = Prize(campaign=campaign)
        form = PrizeForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
        instance = Prize(campaign=campaign)
        form = PrizeForm(instance=instance)
    else:
        form = PrizeForm(instance=instance)
    return render_to_response("create_prize.html", {'form':form, 'all_prizes':prizes_for_campaign, 'campaign':campaign, 'is_saved':is_saved},
        context_instance=RequestContext(request))



def campaign(request, campaign_id):
    campaign = get_object_or_404(Campaign, pk=campaign_id)
    sharing_campaign_user = None
    profiles = None         # profiles is a list of the social networks this user is logged in to.
    posted_to = None        # has the user just posted?  We thank them if so.
    this_users_points = 0   # we use this to calculate how many points they need to win certain prizes

    services = SharingAction.SOCIAL_NETWORK_CHOICES
    actions = SharingAction.objects.filter(action__campaign=campaign, post_or_click=False)

    ###############
    # Leaderboard #
    ###############
    campaign_users = CampaignUser.objects.filter(campaign=campaign)
    # import pdb; pdb.set_trace()
    for campaign_user in campaign_users:
        campaign_user.points = 0
        # get all the actions this user has done by pinging the api call
        # TODO: should we delete any user_actions that are not returned by this call?
        words = campaign.api_call.split(".")
        module = __import__(words[0])
        funct = getattr(module, words[1])
        list_of_actions_ids = funct(campaign)
        # for each element, get or create a new UserAction.
        for action_id in list_of_actions_ids:
            action = get_object_or_None(Action, api_call=action_id, campaign=campaign)
            # create any user actions that don't exist
            if action:
                user_action, created = UserAction.objects.get_or_create(user=campaign_user.user, action=action)
                user_action.save()

        user_actions = UserAction.objects.filter(user=campaign_user.user)

        for user_action in user_actions:
            # call the api for this action.  This returns how many of these actions this user did.
            points_call = user_action.action.api_call
            words = points_call.split(".")
            module = __import__(words[0])
            funct = getattr(module, words[1])
            campaign_user.points += user_action.action.points * funct(campaign_user.user, campaign)
            # if the deadline has passed and the campaign user does not have a points_at_deadline, save this point value
            if campaign.is_past and campaign_user.points_at_deadline == 0:
                campaign_user.points_at_deadline = campaign_user.points

        if campaign_user.user == request.user:
            this_users_points = campaign_user.points

    sorted_campaign_users = sorted(campaign_users, key=lambda o:o.points, reverse=True)
    # import pdb; pdb.set_trace()
    # Bitly sharing link
    this_campaign_user = None
    if request.user.is_authenticated():
        user = request.user
        # create a CampaignUser object - this creates the unique bitly for this user for this campaign      
        this_campaign_user, created = CampaignUser.objects.get_or_create(user=user, campaign=campaign)
        this_campaign_user.save()
        sharing_campaign, created = SharingCampaign.objects.get_or_create(campaign=campaign)
        sharing_campaign_user, created = SharingCampaignUser.objects.get_or_create(sharing_campaign=sharing_campaign, user=this_campaign_user.user)
        sharing_campaign_user.save()
        try:
            user_profile = request.user.get_profile()
            # We replace single quotes with double quotes b/c of python's strict json requirements
            profiles = simplejson.loads(user_profile.profiles.replace("'", '"'))
        except:
            pass

    ##################
    # if they post to social networks:
    ##################
    # TODO: clean up the Sharing module and this stuff -- sharing should not keep accessing ourmy_app models
    if request.method == 'POST': 

        # get the list of social networks the user posted to from the checkboxes
        social_networks_list = request.POST.getlist('social-networks')
        posted_to = ",".join(social_networks_list)        
        body = request.POST['body']
        url = request.POST['url']
        # posting happens in the sharing module
        sharing.post_to_social_networks(user=request.user, social_networks_list=social_networks_list, body=body, url=url, campaign=campaign)

    
    # parse the video url because we're using an embed
    youtube_id = None
    if len(campaign.video_url) > 3:
        if "http://www.youtube.com/watch?v=" in campaign.video_url:
            embed_pieces = campaign.video_url.split("http://www.youtube.com/watch?v=")
        elif "https://www.youtube.com/watch?v=" in campaign.video_url:
            embed_pieces = campaign.video_url.split("https://www.youtube.com/watch?v=")
        if embed_pieces.count > 1:
            id_only = embed_pieces[1].split("&")
            youtube_id = id_only[0]
    
    return render_to_response('campaign.html',
         { 'user':request.user, 'campaign':campaign, 'youtube_id':youtube_id, 'actions':actions, 
           'campaign_users':sorted_campaign_users, 'sharing_campaign_user':sharing_campaign_user, 
           'profiles':profiles, 'posted_to':posted_to, 'this_users_points':this_users_points },
         context_instance=RequestContext(request)
        )


def connect(request, template='connect.html'):
    services = [
        'Facebook',
        # 'foursquare',
        # 'Instagram',
        # 'Tumblr',
        'Twitter',
        'LinkedIn',
        # 'FitBit',
        # 'Email'
    ]
    if request.user.is_authenticated():
        user_profile = request.user.get_profile()
        # We replace single quotes with double quotes b/c of python's strict json requirements
        profiles = simplejson.loads(user_profile.profiles.replace("'", '"'))
    return render_to_response(template, locals(), context_instance=RequestContext(request))

def login(request):
    services = [
        'Facebook',
        # 'foursquare',
        # 'Instagram',
        # 'Tumblr',
        'Twitter',
        # 'LinkedIn',
        # 'FitBit',
        # 'Email'
    ]
    if request.user.is_authenticated():
        user_profile = request.user.get_profile()
        # We replace single quotes with double quotes b/c of python's strict json requirements
        profiles = simplejson.loads(user_profile.profiles.replace("'", '"'))
    return render_to_response('login.html', locals(), context_instance=RequestContext(request))
