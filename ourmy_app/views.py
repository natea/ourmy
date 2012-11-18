from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from ourmy_app.models import Campaign, Action, CampaignUser, UserActions
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
import random
import bitly_api
from django.utils.functional import LazyObject
from ourmy_app.forms import CampaignForm



def index(request):
    # TODO: check that these are current campaigns
    current_campaign_list = Campaign.objects.all()
    return render_to_response('index.html', 
        {'campaign_list':current_campaign_list},
        context_instance=RequestContext(request))


# def create_campaign(request):
#     if request.method == 'POST':
#         try:
#             instance = Campaign.objects.get(user)


def campaign(request, campaign_id):
    campaign = get_object_or_404(Campaign, pk=campaign_id)

    services = [
        'Facebook',
        # 'foursquare',
        # 'Instagram',
        # 'Tumblr',
        'Twitter',
        #'LinkedIn',
        # 'FitBit',
        # 'Email'
    ]
 
    if request.user.is_authenticated():
        try:
            user_profile = request.user.get_profile()
            # We replace single quotes with double quotes b/c of python's strict json requirements
            profiles = simplejson.loads(user_profile.profiles.replace("'", '"'))
        except:
            pass

    # create a CampaignUser object - this creates the unique bitly for this user for this campaign
    if isinstance(request.user, LazyObject):
        user = User(first_name="anonymous", username="anonymous%d" % random.randrange(1,1000000))
        user.save()
    else:
        user = request.user
    
    campaign_user, created = CampaignUser.objects.get_or_create(user=user, campaign=campaign)
    campaign_user.save()

    users = User.objects.all()
    for user in users:
        user.points = random.randrange(1,100)
        # get all the actions this user has done

        user.points = 0
        user_actions = UserActions.objects.filter(user=user)
        # the user gets points for posting
        for user_action in user_actions:
            user.points += user_action.action.points_to_post
        # calculate points for each time their link was clicked
        # TODO: make this based on which social network it is
        connection = bitly_api.Connection(settings.BITLY_LOGIN, settings.BITLY_API_KEY)
        result = connection.clicks(campaign_user.bitly_url)
        user.points += result["clicks"]*user_actions[0]

    response = render_to_response('campaign.html',
         locals(),
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

def post(request, template='post.html'):
    singly = Singly(SINGLY_CLIENT_ID, SINGLY_CLIENT_SECRET)
    user_profile = request.user.get_profile()

    try:
        access_token = user_profile.access_token
    except:
        return

    body = request.POST['body']
    url = request.POST['url']

    payload = {'access_token' : access_token, 
               'to': 'facebook,twitter', 
               'body': body, 
               'url': url}

    success = singly.make_request('/types/news', method='POST', request=payload)

    # if they have posted, we create a UserAction for them and store it in the database
    # if success:
    #     action, created = Action.objects.get_or_create(campaign=)
    #     user_action = UserActions(user=request.user, action=action)
    #     user_action.save()

    response = render_to_response(
            template, locals(), context_instance=RequestContext(request)
        )
    return response