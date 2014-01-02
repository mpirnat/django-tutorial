from django.shortcuts import render, resolve_url
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView

from talks.forms import TalkForm
from talks.models import Talk


class TalkListView(ListView):

    def get_queryset(self):
        return Talk.objects.all_approved()


class TalkCreationView(CreateView):

    model = Talk
    form_class = TalkForm

    def get_success_url(self):
        return resolve_url("accounts:profile")


class TalkUpdateView(UpdateView):

    form_class = TalkForm

    def get_queryset(self):
        return Talk.objects.for_user(self.request.user)

    def get_success_url(self):
        return resolve_url("accounts:profile")

    def get_extra_context_data(self, **kwargs):
        contents = super(TalkUpdateView, self).get_extra_context_data(**kwargs)
        context["editing"] = True
        return context
