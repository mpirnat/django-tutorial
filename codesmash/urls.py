from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'codesmash.views.home', name='home'),
    url(r'^contact/', include('contact.urls', namespace='contact')),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),

    url(r'^admin/', include(admin.site.urls)),
)
