from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'django.contrib.flatpages.views.flatpage',
        {'url': '/' }, name='home'),

    url(r'^contact/', include('contact.urls', namespace='contact')),
    url(r'^accounts/', include('django.contrib.auth.urls', namespace='auth')),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^talks/', include('talks.urls', namespace='talks')),

    url(r'^admin/', include(admin.site.urls)),
)
