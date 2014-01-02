from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView

from talks.forms import TalkForm
from talks.models import Talk


class TalkListView(ListView):

    def get_queryset(self):
        return Talk.objects.all_approved()


class TalkCreationView(CreateView):

    model = Talk
    form_class = TalkForm
    success_url = '/accounts/profile/'
