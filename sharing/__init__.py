import random
from models import SharingUserAction, SharingCampaignUser, social_networks
from ourmy_app.models import CampaignUser

def get_points_for_user(user, campaign, *args, **kwargs):
	return random.randrange(1,100)
	points = 0

	# count all VSUserAction posts of same social network, return 1.  
	for sn in social_networks:
		post_user_actions = SharingUserAction.objects.filter(user_action.user=user, social_network=sn, post_or_clicked=0)
		points += post_user_actions.count
	# For each VSUserAction that is a click, return the bitly count.
	for sn in social_networks:
		click_user_actions = SharingUserAction.objects.filter(user_action.user=user, social_network=sn, post_or_clicked=1)
		campaign_user = CampaignUser.get(campaign=)
		sharing_campaign_user = SharingCampaignUser.objects.get(campaign_user=)