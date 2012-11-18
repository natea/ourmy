from django.contrib import admin
from ourmy_app.models import Campaign, Action, Prize, CampaignUser, UserActions

admin.site.register(Campaign)
admin.site.register(Action)
admin.site.register(Prize)
admin.site.register(CampaignUser)
admin.site.register(UserActions)

