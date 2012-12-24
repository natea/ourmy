from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'ourmy_app.views.index', name='home'),
    url(r'^connect$', 'ourmy_app.views.connect', name='connect'),
    url(r'^test_bootstrap/', include('test_bootstrap.urls')),
    # url(r'^ourmy/', include('ourmy.foo.urls')),

    url(r'^campaign/(?P<campaign_id>\d{0,6})/$', 'ourmy_app.views.campaign', name='campaign'),
    url(r'^create_campaign$', 'ourmy_app.views.create_campaign', name='create_campaign'),
    url(r'^edit_campaign/(?P<campaign_id>\d{0,6})/$', 'ourmy_app.views.create_campaign', name='edit_campaign'),
    url(r'^create_prize/(?P<campaign_id>\d{0,6})/$', 'ourmy_app.views.create_prize', name='create_prize'),
    url(r'^edit_prize/(?P<prize_id>\d{0,6})/$', 'ourmy_app.views.create_prize', name='edit_prize'),

    # url(r'^sharing/', include("sharing.urls", namespace="sharing")),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^login/$', 'ourmy_app.views.campaign', name='login'),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
	# url("^$", direct_to_template, {"template": "index.html"}, name="home"),
    url(r'', include('singly.urls')),
)
