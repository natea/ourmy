import random
import bitly_api

from django.conf import settings

from models import SharingCampaign, SharingUserAction, SharingCampaignUser, SharingAction
from ourmy_app.models import CampaignUser
from annoying.functions import get_object_or_None


def get_points_for_user(user, *args, **kwargs):
	return random.randrange(1,100)
	# points = 0

	# # count all VSUserAction posts of same social network, return 1.  
	# for sn in SharingUserAction.SOCIAL_NETWORKS:
	# 	post_user_actions = SharingUserAction.objects.filter(user_action.user=user, social_network=sn, post_or_clicked=0)
	# 	points += post_user_actions.count
	# # For each VSUserAction that is a click, return the bitly count.
	# for sn in SharingUserAction.SOCIAL_NETWORKS:
	# 	click_user_actions = SharingUserAction.objects.filter(user_action.user=user, social_network=sn, post_or_clicked=1)

def get_actions_for_campaign(campaign):
	# this should return a list of api calls that will return points values for the various user actions.
	# return ["get_facebook_post_points_for_user", "get_facebook_click_points_for_user", "get_twitter_post_points_for_user", "get_twitter_click_points_for_user"]
	sharing_actions = SharingAction.objects.filter(action__campaign=campaign)
	# print campaign
	# print sharing_actions
	# print [x.action.api_call for x in sharing_actions]
	return [x.action.api_call for x in sharing_actions]

def get_facebook_post_actions_for_user(user, campaign):
	# n = random.randrange(1,100)
	services = SharingAction.SOCIAL_NETWORK_CHOICES
	sharing_user_actions = SharingUserAction.objects.filter(user=user, 
								sharing_action__social_network=services[0], 
								sharing_action__action__campaign=campaign,
								sharing_action__post_or_click=False)
	# print "called get_facebook_post_points_for_user, returning "
	# print len(sharing_user_actions)
	return len(sharing_user_actions)

def get_click_actions_for_user(user, campaign, *args, **kwargs):
	sharing_campaign = get_object_or_None(SharingCampaign, campaign=campaign)
	clicks = 0
	if sharing_campaign:
		sharing_campaign_user = get_object_or_None(SharingCampaignUser, user=user, sharing_campaign=sharing_campaign)
		
		if sharing_campaign_user:
			sharable_url = sharing_campaign_user.sharable_url

			if sharable_url:
				connection = bitly_api.Connection(settings.BITLY_LOGIN, settings.BITLY_API_KEY)
				bitly_hash = sharable_url.split('/')[-1]
				# print connection.clicks(bitly_hash)
				clicks = connection.clicks(bitly_hash)[0]['global_clicks']
				# TODO: add the Facebook referrers
				# https://github.com/bitly/bitly-api-python/blob/master/bitly_api/bitly_api.py#L107

	# add the number of posts
	return clicks

def get_twitter_post_actions_for_user(user, campaign):
	services = SharingAction.SOCIAL_NETWORK_CHOICES
	sharing_user_actions = SharingUserAction.objects.filter(user=user, 
								sharing_action__social_network=services[0], 
								sharing_action__action__campaign=campaign,
								sharing_action__post_or_click=True)
	# print "called get_twitter_post_points_for_user, returning "
	# print len(sharing_user_actions)
	return len(sharing_user_actions)