from django.conf.urls import patterns, include, url


urlpatterns = patterns('talks.views',
    url(r'^$', 'all_talks', name='index'),
)
