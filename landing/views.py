from django.shortcuts import render


def index_view(request):
    return render(request, "landing/index.html")


def about_view(request):
    return render(request, "landing/about.html")
