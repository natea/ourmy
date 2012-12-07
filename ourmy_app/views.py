from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from ourmy_app.models import Campaign, Action, CampaignUser, UserAction
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
from ourmy_app.forms import CampaignForm
from django.utils.functional import LazyObject
import sharing
from sharing import get_points_for_user
from sharing.models import SharingCampaign, SharingCampaignUser
from annoying.functions import get_object_or_None


def index(request):
    # TODO: check that these are current campaigns
    current_campaign_list = Campaign.objects.all()
    return render_to_response('index.html', 
        {'campaign_list':current_campaign_list},
        context_instance=RequestContext(request))

@login_required
def create_campaign(request, campaign_id=None):
    instance=None
    campaigns = []
    campaigns = Campaign.objects.filter(user=request.user)
    if request.method == 'POST':
        if campaign_id is not None:
            campaign = get_object_or_404(Campaign, pk=campaign_id)
            sharing_campaign = SharingCampaign.objects.get(campaign=campaign)
            form = CampaignForm(initial={'title':campaign.title, 'long_url':sharing_campaign.long_url})
        else:
            form = CampaignForm(request.POST)
            
        if form.is_valid():
            campaign = Campaign(user=request.user, title=request.POST['title'], api_call="get_actions_for_user")
            campaign.save()
            sharing_campaign = SharingCampaign(campaign=campaign, long_url=request.POST['long_url'])
            sharing_campaign.save()
            print "should have saved a campaign and sharing_campaign"
            return HttpResponseRedirect("/")
    else:
        if campaign_id is not None:
            campaign = get_object_or_404(Campaign, pk=campaign_id)
            sharing_campaign = SharingCampaign.objects.get(campaign=campaign)
            form = CampaignForm(initial={'title':campaign.title, 'long_url':sharing_campaign.long_url})
        else:
            form = CampaignForm()
    return render_to_response("create_campaign.html", {'form':form, 'campaigns':campaigns},
        context_instance=RequestContext(request))


def campaign(request, campaign_id):
    campaign = get_object_or_404(Campaign, pk=campaign_id)
    sharing_campaign_user = None
    profiles = None

    services = [
        'facebook',
        # 'foursquare',
        # 'Instagram',
        # 'Tumblr',
        'twitter',
        #'LinkedIn',
        # 'FitBit',
        # 'Email'
    ]

    # Leaderboard
    users = User.objects.all()
    for user in users:
        user.points = 0
        # get all the actions this user has done by pinging the CampaignUser's api call
        # TODO: should we delete any user_actions that are not returned by this call?
        campaign_user = get_object_or_None(CampaignUser, pk=user.id)
        if campaign_user:
            words = campaign_user.campaign.api_call.split(".")
            module = __import__(words[0])
            funct = getattr(module, words[1])
            list_of_actions_ids = funct(user)
            # for each element, get or create a new UserAction.
            for action_id in list_of_actions_ids:
                action = get_object_or_None(Action, api_call=action_id)
                # create any actions that don't exist
                if action:
                    user_action, created = UserAction.get_or_create(user=user, action=action)
                    user_action.save()

        user_actions = UserAction.objects.filter(user=user)

        for user_action in user_actions:
            # call the api for this action.  This returns how many of these actions this user did.
            points_call = user_action.action.api_call
            words = points_call.split(".")
            module = __import__(words[0])
            funct = getattr(module, words[1])
            user.points += user_action.action.points * funct(user)


        # calculate points for each time their link was clicked
        # TODO: make this based on which social network it is
        # connection = bitly_api.Connection(settings.BITLY_LOGIN, settings.BITLY_API_KEY)
        # result = connection.clicks(campaign_user.bitly_url)
        # user.points += result["clicks"]*user_actions[0]
        # user.points += get_points_for_user(user)
        # points_calls = ["sharing.get_facebook_post_points_for_user", "sharing.get_facebook_click_points_for_user", "sharing.get_twitter_post_points_for_user", "sharing.get_twitter_click_points_for_user"]

        # points_calls = Action.objects.filter(campaign=campaign).values_list('api_call', flat=True)
        # for element in points_calls:
        #     words = element.split(".")
        #     module = __import__(words[0])
        #     funct = getattr(module, words[1])
        #     user.points += funct(user)
    sorted_users = sorted(users, key=lambda o:o.points, reverse=True)

 
    # Bitly sharing link
    campaign_user = None
    if request.user.is_authenticated():
        user = request.user
        # create a CampaignUser object - this creates the unique bitly for this user for this campaign      
        campaign_user, created = CampaignUser.objects.get_or_create(user=user, campaign=campaign)
        if created: print "the campaign user was created"
        campaign_user.save()
        sharing_campaign, created = SharingCampaign.objects.get_or_create(campaign=campaign)
        if created: print "the campaign user was created"
        sharing_campaign_user, created = SharingCampaignUser.objects.get_or_create(sharing_campaign=sharing_campaign, user=user)
        if created: 
            print "the campaign user was created"
        sharing_campaign_user.save()
        try:
            user_profile = request.user.get_profile()
            # We replace single quotes with double quotes b/c of python's strict json requirements
            profiles = simplejson.loads(user_profile.profiles.replace("'", '"'))
        except:
            pass
    
    # campaign_user, created = CampaignUser.objects.get_or_create(user=user, campaign=campaign)
    # campaign_user.save()

    if request.method == 'POST':
        singly = Singly(SINGLY_CLIENT_ID, SINGLY_CLIENT_SECRET)
        try:
            user_profile = request.user.get_profile()
            try:
                access_token = user_profile.access_token
            except:
                pass

            body = request.POST['body']
            url = request.POST['url']

            payload = {'access_token' : access_token, 
                       'services': 'facebook,twitter', 
                       'body': body, 
                       'url': url
                       }

            return_data = singly.make_request('/types/news', method='POST', request=payload)
            for service in services:
                try:
                    success = return_data[service]['id']
                    action, created = Action.objects.get_or_create(campaign=campaign, social_network=service)
                    user_action = UserAction(user=request.user, action=action)
                    user_action.save()
                except:
                    pass
        except:
            print "drat - no singly profile"

        # if they have posted, we create a UserAction for them and store it in the database
        # if success:

    response = render_to_response('campaign.html',
         { 'campaign':campaign, 'user':request.user, 'services':services, 
           'users':sorted_users, 'sharing_campaign_user':sharing_campaign_user, 'profiles':profiles },
         context_instance=RequestContext(request)
        )
    return response


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
    response = render_to_response(
            template, locals(), context_instance=RequestContext(request)
        )
    return response

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
    response = render_to_response('login.html', locals(), context_instance=RequestContext(request)
        )
    return response
