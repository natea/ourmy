from django import forms
from ourmy_app.models import Campaign, Prize


class CampaignForm(forms.ModelForm):
    class Meta:
        model = Campaign
        exclude = ('user','api_call', 'video_url') # change ZT001: remove this temporarily until we can promtoe non-video urls

    title = forms.CharField(label="Title of your campaign")
    # ZT001:  remove this temporarily until we can promote non-video urls
    # video_url = forms.CharField(label="Url of the youtube video you want to appear in your campaign")
    post_text = forms.CharField(label="The text you want to appear in social media posts before the link:")
    long_url = forms.URLField(label="URL you want your fans to promote")

class PrizeForm(forms.ModelForm):
    class Meta:
        model = Prize
        exclude = ('campaign')

    video_url = forms.URLField(label="Have a video that shows off this prize?  Put the link right here (Note: Currently only accept YouTube URLs in this field):", required=False)
    dollar_value = forms.DecimalField(label="The dollar value of this prize (We'll add the $ sign):")
    points_value = forms.IntegerField(label="What is the minimum number of points a user has to get before they are eligible to win this prize?")
    how_many = forms.IntegerField(label="How many of these prizes will you give away?")
    place = forms.IntegerField(label="If this prize goes only to the first place winner (above the points value), put 1.  Second place, put 2, etc.")
    chance = forms.NullBooleanField(label="Do you want your users to only have a 'chance' of winning this prize?  If 'Yes', the people who win will be randomly chosen from among those that reached the required points.  If 'No', the top people will win the prize.")