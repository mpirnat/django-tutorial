from django.shortcuts import render
from django.views.generic import ListView

from talks.models import Talk


class TalkListView(ListView):

    def get_queryset(self):
        return Talk.objects.all_approved()
