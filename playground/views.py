from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item
from .forms import CreateNewList
# Create views here

def index(response, id):
    ls = ToDoList.objects.get(id=id)
    return render(response, "playground/list.html", {"ls": ls})


def home(response):
    return render(response, "playground/home.html", {})


def create(response):
    form = CreateNewList()
    return render(response, "playground/create.html", {"form": form})
