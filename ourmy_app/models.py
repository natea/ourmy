from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import datetime
import os
    
class UserProfile(models.Model):
    bio = models.TextField()
    user = models.ForeignKey(User, unique=True)
    
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

	class Admin:
		list_display = ('',)
		search_fields = ('',)

	def __unicode__(self):
		return self.title

class Prize(models.Model):
	campaign = models.ForeignKey(Campaign)
	title = models.CharField(max_length=100)
	logo_image = models.FileField(upload_to=get_prize_logo_path, blank=True, null=True)
	description = models.TextField(blank=True, max_length=250)	
	value = models.DecimalField(max_digits=6, decimal_places=2)

	def __unicode__(self):
		return self.title + ' for ' + self.campaign.title


class Action(models.Model):
	campaign = models.ForeignKey(Campaign)
	social_network = models.CharField(max_length=100)
	text = models.TextField(blank=True)
	points = models.IntegerField(default=1)
	start_on = models.DateTimeField(blank=True, default=datetime.datetime.now)
	end_on = models.DateTimeField(blank=True, default=datetime.datetime.now)

	def __unicode__(self):
		return self.campaign.title + ': ' + self.social_network


class UserActions(models.Model):
	user = models.ForeignKey(User)
	action = models.ForeignKey(Action)

	def __unicode__(self):
		return self.user.username + ' on ' + action.social_network