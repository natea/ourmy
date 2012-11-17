from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ourmy_app.models import Campaign, Action
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib.sites.models import get_current_site
from django.template import loader
import datetime
import simplejson

def index(request):
	# TODO: check that these are current campaigns
	current_campaign_list = Campaign.objects.all()
	return render_to_response('index.html', 
		{'campaign_list':current_campaign_list},
		context_instance=RequestContext(request))


def campaign(request, campaign_id):
	campaign = get_object_or_404(Campaign, pk=campaign_id)
	return render_to_response('campaign.html',
		{'campaign':campaign},
		context_instance=RequestContext(request))

def connect(request, template='connect.html'):
    services = [
        'Facebook',
        # 'foursquare',
        # 'Instagram',
        # 'Tumblr',
        'Twitter',
        'LinkedIn',
        # 'FitBit',
        # 'Email'
    ]
    if request.user.is_authenticated():
        user_profile = request.user.get_profile()
        # We replace single quotes with double quotes b/c of python's strict json requirements
        profiles = simplejson.loads(user_profile.profiles.replace("'", '"'))
    response = render_to_response(
            template, locals(), context_instance=RequestContext(request)
        )
    return response
