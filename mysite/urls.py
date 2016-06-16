from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    'mysite.bands.views',
    url(r'^$', 'home', name='home'),
    url(r'^admin/', include(admin.site.urls), name='admin'),
)
