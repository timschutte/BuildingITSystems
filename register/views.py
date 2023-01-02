from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("http://127.0.0.1:8000")
    else:
        form = RegisterForm()
    return render(response, "register/register.html", {"form": form})

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
    
    if user is not None:
        login(request, user)
        return redirect('playground/schedule.html')
    else:
        messages.info(request, 'Username OR password is incorrect')
    return render(request, 'registration/login.html')

def logoutUser(request):
    logout(request)
    return redirect('registration/login.html')