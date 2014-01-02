from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from accounts.forms import RegistrationForm


def profile(request):
    return render(request, "accounts/profile.html")


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
