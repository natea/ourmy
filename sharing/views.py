from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from ourmy_app.models import Campaign, Action, CampaignUser, UserAction
from django.http import HttpResponseRedirect, Http404, HttpResponse
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
from sharing.models import SharingCampaign, SharingCampaignUser
from annoying.functions import get_object_or_None


import random
# import bitly_api

# from django.conf import settings

# from models import SharingUserAction, SharingCampaignUser
# from ourmy_app.models import CampaignUser

from annoying.decorators import ajax_request

# @ajax_request
def get_facebook_post_points_for_user(reqeust):  #, user, *args, **kwargs):
	# print "called get_facebook_post_points_for_user"
	points = random.randrange(1,100)
	points = 34
	return {'points':points, 'something':"hi there"}
	# return HttpResponse("does this view work?")


# def get_points_for_user(user, *args, **kwargs):
# 	return random.randrange(1,100)
# 	# points = 0

# 	# # count all VSUserAction posts of same social network, return 1.  
# 	# for sn in SharingUserAction.SOCIAL_NETWORKS:
# 	# 	post_user_actions = SharingUserAction.objects.filter(user_action.user=user, social_network=sn, post_or_clicked=0)
# 	# 	points += post_user_actions.count
# 	# # For each VSUserAction that is a click, return the bitly count.
# 	# for sn in SharingUserAction.SOCIAL_NETWORKS:
# 	# 	click_user_actions = SharingUserAction.objects.filter(user_action.user=user, social_network=sn, post_or_clicked=1)

# def get_actions_for_user(user):
# 	return ["get_facebook_post_points_for_user", "get_facebook_click_points_for_user", "get_twitter_post_points_for_user", "get_twitter_click_points_for_user"]

# def get_facebook_click_points_for_user(user, campaign, *args, **kwargs):
# 	sharing_campaign = get_object_or_None(SharingCampaign, campaign=campaign)
# 	clicks = 0
# 	if sharing_campaign:
# 		sharing_campaign_user = get_object_or_None(SharingCampaignUser, user=user, sharing_campaign=sharing_campaign)
		
# 		if sharing_campaign_user:
# 			sharable_url = sharing_campaign_user.sharable_url

# 			if sharable_url:
# 				connection = bitly_api.Connection(settings.BITLY_LOGIN, settings.BITLY_API_KEY)
# 				bitly_hash = sharable_url.split('/')[-1]
# 				clicks = connection.clicks(bitly_hash)[0]['global_clicks']
# 				# TODO: add the Facebook referrers
# 				# https://github.com/bitly/bitly-api-python/blob/master/bitly_api/bitly_api.py#L107

# 	return clicks

# def get_twitter_post_points_for_user(user, *args, **kwargs):
# 	print "called get_twitter_post_points_for_user"
# 	return random.randrange(1,100)

# def get_twitter_click_points_for_user(user, *args, **kwargs):
# 	print "called get_twitter_click_points_for_user"
# 	return random.randrange(1,100)