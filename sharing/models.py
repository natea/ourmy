import bitly_api

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from ourmy_app.models import Campaign, CampaignUser, UserAction


class SharingCampaign(models.Model):
    campaign = models.ForeignKey(Campaign, unique=True)
    long_url = models.URLField(default="http://zoomtilt.com")

    def __unicode__(self):
        return self.campaign.title + ' ' + self.long_url

class SharingCampaignUser(models.Model):
    sharing_campaign = models.ForeignKey(SharingCampaign)
    user = models.ForeignKey(User)
    sharable_url = models.URLField()

    def __unicode__(self):
        return self.sharing_campaign.campaign.title + ' ' + self.user.last_name

    def save(self, *args, **kwargs):
        connection = bitly_api.Connection(settings.BITLY_LOGIN, settings.BITLY_API_KEY)
        result = connection.shorten(self.sharing_campaign.long_url)
        self.sharable_url = result["url"]
        super(SharingCampaignUser, self).save(*args, **kwargs)      # Call the "real" save() method.

class SharingUserAction(models.Model):
    FACEBOOK = 'FB'
    TWITTER = 'TW'
    SOCIAL_NETWORK_CHOICES = (
        (FACEBOOK, 'facebook'),
        (TWITTER, 'twitter'),
    )

    user_action = models.ForeignKey(UserAction)
    social_network = models.CharField(max_length=2, choices=SOCIAL_NETWORK_CHOICES, default=FACEBOOK)
    post_or_clicked = models.BooleanField()
    last_checked = models.DateTimeField(auto_now_add=True)  # check that auto now add does what I want...