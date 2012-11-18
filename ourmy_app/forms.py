from django import forms
from ourmy_app.models import Campaign

class CampaignForm(forms.Form):

	class Meta:
		model = Campaign