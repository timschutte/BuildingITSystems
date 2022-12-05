from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path("<str:id>", views.index, name="index"),
    path("", views.home, name="home"),
    path("create/", views.create, name="create"),
]

# start/
