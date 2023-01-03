from django.shortcuts import render, HttpResponse
from . import index


def home(request):
    html = index.weekscheduleHTML(1, 1)
    return HttpResponse(html)