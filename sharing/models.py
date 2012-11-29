from django.db import models
from ourmy_app.models import Campaign, CampaignUser, UserAction

social_networks = ['facebook','twitter']

class SharingCampaign(models.Model):
	campaign = models.ForeignKey(Campaign)
    long_url = models.URLField(default="http://zoomtilt.com")

    def __unicode__(self):
    	return self.campaign.title + ' ' + self.long_url

class SharingCampaignUser(models.Model):
	campaign_user = models.ForeignKey(CampaignUser)
    sharable_url = models.URLField()

    def __unicode__(self):
    	return self.campaign_user.campaign.title + ' ' + self.campaign_user.user.last_name

class SharingUserAction(models.Model):
	user_action = models.ForeignKey(UserAction)
	social_network = models.CharField()		# select from social_networks
	post_or_clicked = models.BooleanField()
	last_checked = models.DateTimeField(auto_now_add=True)	# check that auto now add does what I want...