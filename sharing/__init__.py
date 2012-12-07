import random
from models import SharingUserAction, SharingCampaignUser
from ourmy_app.models import CampaignUser

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

def get_actions_for_user(user):
	return ["get_facebook_post_points_for_user", "get_facebook_click_points_for_user", "get_twitter_post_points_for_user", "get_twitter_click_points_for_user"]

def get_facebook_post_points_for_user(user, *args, **kwargs):
	print "called get_facebook_post_points_for_user"
	return random.randrange(1,100)

def get_facebook_click_points_for_user(user, *args, **kwargs):
	print "called get_facebook_click_points_for_user"
	return random.randrange(1,100)

def get_twitter_post_points_for_user(user, *args, **kwargs):
	print "called get_twitter_post_points_for_user"
	return random.randrange(1,100)

def get_twitter_click_points_for_user(user, *args, **kwargs):
	print "called get_twitter_click_points_for_user"
	return random.randrange(1,100)