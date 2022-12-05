from django.shortcuts import render

def login(response):
    pass

def home(response):
    return render(response,"scheduling/index.html")
    
