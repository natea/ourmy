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
