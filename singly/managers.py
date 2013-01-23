"""
Based on Singly django example:
https://github.com/Singly/python_django_skeleton/tree/master/singly
"""

import random

from django.db import models
from singly import *
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

def GenerateUsername():
    i = 0
    MAX = 1000000
    while(i < MAX):
        username = str(random.randint(0,MAX))
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
    raise Exception('All random username are taken')


class UserProfileManager(models.Manager):

    def get_or_create_user(self, singly_id, access_token):
        # endpoint = '/profiles'
        # request = {'auth': 'true'}
        # profiles = Singly(access_token=access_token).make_request(endpoint, request=request)
        # singly_id = profiles['id']
        # try:
        #     user_profile = self.get(singly_id=singly_id)
        #     user_profile.profiles = profiles
        #     user_profile.save()

        # except ObjectDoesNotExist:
        #     try:
        #         user = User.objects.get(username=singly_id)
        #     except ObjectDoesNotExist:
        #         # Made-up email address included due to convention
        #         user = User.objects.create_user(singly_id, singly_id + '@singly.com', 'fakepassword')
        #     user_profile = self.model(
        #         access_token=access_token,
        #         singly_id=singly_id,
        #         profiles=profiles,
        #         user=user
        #     )
        #     user_profile.save()
        # return user_profile

        endpoint = '/profiles'
        request = {'auth': 'true'}
        profiles = Singly(access_token=access_token).make_request(endpoint, request=request)
        singly_id = profiles['id']

#-------
        endpoint = '/profile'
        profile = Singly(access_token=access_token).make_request(endpoint, request=request)

        email = ''
        if 'email' in profile:
            email = profile['email']
        if 'name' in profile:
            name = profile['name']
            first_name = profile['name'].split(' ')[0]
            last_name = profile['name'].split(' ')[-1]    
        
        if 'thumbnail_url' in profile:
            if profile['thumbnail_url'] != '':
                thumbnail_url = profile['thumbnail_url']

        try:
            # get the user if it already exists
            user = User.objects.get(profile__singly_id=singly_id)

        except ObjectDoesNotExist:
            # if there is no user yet, create one
            # Made-up password address included due to convention
            username = GenerateUsername()
            user = User.objects.create_user(username, email, 'fakepassword')
            
            if name:
                user.first_name = first_name
                user.last_name = last_name
            user.save()

            # create a user profile
            user_profile = self.model(
                access_token=access_token,
                singly_id=singly_id,
                handle=handle,
                profiles=profiles,
                user=user,
                profile=profile,
                thumbnail_url=thumbnail_url
            )
            user_profile.save()

        # update the user profile information in case anything has changed
        user_profile = self.get(singly_id=singly_id)
        user_profile.handle = handle
        user_profile.profiles = profiles
        user_profile.profile = profile
        user_profile.thumbnail_url = thumbnail_url
        user_profile.user = user

        return user_profile
