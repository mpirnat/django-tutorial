from django.conf.urls import patterns, include, url

from talks.views import TalkListView


urlpatterns = patterns('talks.views',
    url(r'^$', TalkListView.as_view(), name='index'),
)
