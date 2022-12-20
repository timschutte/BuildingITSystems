from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create views here


def index(response):
    return render(response, "playground/index.html", {})


def messages(request):
    return render(request, 'playground/messages.html')


def profile(request):
    return render(request, 'playground/profile.html')


def schedule(request):
    return render(request, 'playground/schedule.html')


def about(request):
    return render(request, 'playground/about.html')
