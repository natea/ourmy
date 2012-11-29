import datetime
import os

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.conf import settings

from singly.models import SinglyProfile
import bitly_api
    
class UserProfile(SinglyProfile):
    bio = models.TextField()
    
    def __unicode__(self):
        return self.user.username
    
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


def get_campaign_logo_path(instance, filename):
    return os.path.join('logos', "%d_%s" % (instance.user.id, filename))

def get_prize_logo_path(instance, filename):
    return os.path.join('logos', "%d_%s" % (instance.campaigng.user.id, filename))


class Campaign(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(blank=True, max_length=100)
    description = models.TextField(blank=True, max_length=250)
    deadline = models.DateTimeField(blank=True, default=datetime.datetime.now)
    logo_image = models.FileField(upload_to=get_campaign_logo_path, blank=True, null=True)
    video_url = models.URLField(blank=True)

    class Admin:
        list_display = ('',)
        search_fields = ('',)

    def __unicode__(self):
        return self.title

class Prize(models.Model):
    campaign = models.ForeignKey(Campaign)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, max_length=250)  
    logo_image = models.FileField(upload_to=get_prize_logo_path, blank=True, null=True)
    video_url = models.URLField(blank=True)
    dollar_value = models.DecimalField(max_digits=6, decimal_places=2, default=10)
    points_value = models.IntegerField(default=100)
    how_many = models.IntegerField(default=1)
    place = models.IntegerField(default=1)
    chance = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title + ' for ' + self.campaign.title


class CampaignUser(models.Model):
    campaign = models.ForeignKey(Campaign)
    user = models.ForeignKey(User)
    api_call = models.CharField(max_length=500)
    # bitly_url = models.CharField(max_length=100)
    last_checked = models.DateTimeField(default=datetime.datetime.now)
    # stats = models.TextField(blank=True, max_length=400)

    def save(self, *args, **kwargs):
        connection = bitly_api.Connection(settings.BITLY_LOGIN, settings.BITLY_API_KEY)
        result = connection.shorten(self.campaign.long_url)
        self.bitly_url = result["url"]
        super(CampaignUser, self).save(*args, **kwargs)      # Call the "real" save() method.

	def __unicode__(self):
		return self.title + ' for ' + self.campaign.title



class Action(models.Model):
    campaign = models.ForeignKey(Campaign)
    # social_network = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    logo_image = models.FileField(upload_to=get_prize_logo_path, blank=True, null=True)
    video_url = models.URLField(blank=True)
    points = models.IntegerField(default=1)
    # points_to_post = models.IntegerField(default=10)
    # points_per_click = models.IntegerField(default=1)
    start_at = models.DateTimeField(blank=True, default=datetime.datetime.now)
    end_at = models.DateTimeField(blank=True, default=datetime.datetime.now)
    api_call = models.CharField(max_length=500)
    last_checked = models.DateTimeField(default=datetime.datetime.now)

    def __unicode__(self):
        return self.campaign.title + ': ' + self.social_network


class UserActions(models.Model):
    user = models.ForeignKey(User)
    action = models.ForeignKey(Action)

    def __unicode__(self):
        return self.user.username + ' on ' + action.social_network
