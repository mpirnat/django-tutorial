from django.conf.urls import patterns, include, url


urlpatterns = patterns('accounts.views',
    url(r'^create/$', 'create_user', name='create'),
    url(r'^profile/$', 'profile', name='profile'),
)
