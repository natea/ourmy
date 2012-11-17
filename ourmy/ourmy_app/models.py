from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import datetime
    
class UserProfile(models.Model):
    bio = models.TextField()
    user = models.ForeignKey(User, unique=True)
    
    def __unicode__(self):
        return self.user.username
    
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


class Campaign(models.Model):
	user = models.ForeignKey(User)
	description = models.TextField(blank=True, max_length=250)
	deadline = models.DateTimeField(blank=True, default=datetime.datetime.now)
	# logo_image = models.FileField(upload_to=get_logo_path, blank=True, null=True)


class Action(models.Model):
	campaign = models.ForeignKey(Campaign)
	social_network = models.CharField(max_length=100)
	text = models.TextField(blank=True)
	points = models.IntegerField(default=1)
	start_on = models.DateTimeField(blank=True, default=datetime.datetime.now)
	end_on = models.DateTimeField(blank=True, default=datetime.datetime.now)


class UserActions(models.Model):
	user = models.ForeignKey(User)
	action = models.ForeignKey(Action)