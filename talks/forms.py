from django import forms

from talks.models import Talk


class TalkForm(forms.ModelForm):

    class Meta:
        model = Talk
        exclude = ("approved", "location", "time_slot")
