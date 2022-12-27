from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from .forms import RegisterForm

def index(request):
   return render(request, 'Scheduling/index.html')

def messages(request):
    return render(request, 'Scheduling/messages.html')

def profile(request):
    return render(request, 'Scheduling/profile.html')

def schedule(request):
    return render(request, 'Scheduling/schedule.html')

def about(request):
    return render(request, 'Scheduling/about.html')

def login(request):
    return render(request, 'Scheduling/login.html')

def test(request):
    return render(request, 'Scheduling/test.html')

def footer(request):
    return render(request, 'Scheduling/footer.html')

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("/home")
    else:
        form = RegisterForm()
    return render(response, "register/register.html", {"form": form})


