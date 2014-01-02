from django.shortcuts import render


def home(request):
    """The home page view
    """
    return render(request, "index.html")
