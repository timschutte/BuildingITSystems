from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create views here


def index(request):
    return render(request, "playground/index.html", {})


def messages(request):
    return render(request, 'playground/messages.html')


def profile(request):
    return render(request, 'playground/profile.html')


def schedule(request):
    return render(request, 'playground/schedule.html')


def about(request):
    return render(request, 'playground/about.html')

def test(request):
    return render(request, 'playground/test.html')

def footer(request):
    return render(request, 'playground/footer.html')

def calender(request):
    return render(request, 'playground/calender.html')


