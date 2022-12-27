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
