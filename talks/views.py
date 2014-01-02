from django.shortcuts import render

from talks.models import Talk


def all_talks(request):
    return render(request, "talks/index.html", {
        "all_talks": Talk.objects.all_approved(),
    })
