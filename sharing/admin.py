from django.contrib import admin
from models import SharingCampaign, SharingCampaignUser, SharingAction, SharingUserAction

admin.site.register(SharingCampaign)
admin.site.register(SharingCampaignUser)
admin.site.register(SharingAction)
admin.site.register(SharingUserAction)