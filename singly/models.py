from django.contrib.auth.models import User
from django.db import models
from managers import UserProfileManager


class SinglyProfile(models.Model):
    access_token = models.CharField(max_length=260, null=True, blank=True)
    singly_id = models.CharField(max_length=260, null=True, blank=True)
    # each social network has its own profile in profiles
    profiles = models.TextField(null=True, blank=True)
    # data that singly has that is unique to the user but same for diff social networks
    profile = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, related_name='profile')
    # we're grabbing this so we can display the user's pic
    thumbnail_url = models.URLField(max_length=260, blank=True, default='')
    handle = models.CharField(max_length=260, null=True, blank=True)

    objects = UserProfileManager()

    class Meta:
        db_table = 'user_profile'

    def __unicode__(self):
        return self.user.first_name + ' ' + self.user.last_name + ' ' + self.singly_id