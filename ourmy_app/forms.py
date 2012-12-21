from django import forms
from ourmy_app.models import Campaign


class CampaignForm(forms.Form):

    title = forms.CharField(label="Title of your campaign", max_length=100)
    post_text = forms.CharField(max_length=120, label="The text you want to appear in social media posts before the link:")
    long_url = forms.URLField(label="URL you want your fans to promote")
