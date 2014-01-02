from django import forms
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):

    email = forms.EmailField(required=True, help_text="Required.")

    class Meta(UserCreationForm.Meta):
        fields = ("username", "email")
