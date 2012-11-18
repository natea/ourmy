import datetime
import simplejson
import random
import urllib

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib.sites.models import get_current_site
from django.template import loader

from singly.singly import Singly

from ourmy_project.settings import SINGLY_CLIENT_ID, SINGLY_CLIENT_SECRET, SINGLY_REDIRECT_URI
from ourmy_app.models import Campaign, Action

def index(request):
    # TODO: check that these are current campaigns
    current_campaign_list = Campaign.objects.all()
    return render_to_response('index.html', 
        {'campaign_list':current_campaign_list},
        context_instance=RequestContext(request))


def campaign(request, campaign_id):
    campaign = get_object_or_404(Campaign, pk=campaign_id)

    services = [
        'Facebook',
        # 'foursquare',
        # 'Instagram',
        # 'Tumblr',
        'Twitter',
        #'LinkedIn',
        # 'FitBit',
        # 'Email'
    ]
 
    if request.user.is_authenticated():
        try:
            user_profile = request.user.get_profile()
            # We replace single quotes with double quotes b/c of python's strict json requirements
            profiles = simplejson.loads(user_profile.profiles.replace("'", '"'))
        except:
            pass

    users = User.objects.all()
    for user in users:
        user.points = random.randrange(1,100)

    response = render_to_response('campaign.html',
         locals(),
         context_instance=RequestContext(request)
        )
    return response


def post(request, template='post.html'):
    singly = Singly(SINGLY_CLIENT_ID, SINGLY_CLIENT_SECRET)
    user_profile = request.user.get_profile()

    try:
        access_token = user_profile.access_token
    except:
        return

    url = request.POST['url']
    body = request.POST['body']

    payload = {'access_token' : access_token, 
               'services': 'facebook,twitter', 
               'body': body, 
               'url': url}

    success = singly.make_request('/types/news', method='POST', request=payload)

    response = render_to_response(
            template, locals(), context_instance=RequestContext(request)
        )
    return response