from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from accounts.forms import RegistrationForm
from talks.models import Talk


def profile(request):
    return render(request, "accounts/profile.html", {
        'proposals': Talk.objects.for_user(request.user),
    })


def create_user(request):
    form = RegistrationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()

        user = authenticate(username=form.cleaned_data["username"],
                password=form.cleaned_data["password1"])
        login(request, user)

        return redirect("accounts:profile")

    return render(request, "accounts/create.html", {
        "form": form,
    })
