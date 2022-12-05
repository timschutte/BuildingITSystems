from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


def index(request):
   return render(request, 'index.html')

def messages(request):
    return render(request, 'messages.html')

def profile(request):
    return render(request, 'profile.html')

def schedule(request):
    return render(request, 'schedule.html')

def about(request):
    return render(request, 'about.html')