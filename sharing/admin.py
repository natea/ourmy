from django.contrib import admin
from models import SharingCampaign, SharingCampaignUser, SharingUserAction

admin.site.register(SharingCampaign)
admin.site.register(SharingCampaignUser)
admin.site.register(SharingUserAction)