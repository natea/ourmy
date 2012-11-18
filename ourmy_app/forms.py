from django import forms
from ourmy_app.models import Campaign

class CampaignForm(forms.ModelForm):

    class Meta:
        model = Campaign
        fields = ('title','long_url',)

    title = forms.CharField(label="Title of your campaign", max_length=100)
    long_url = forms.URLField(label="URL you want your fans to promote")