
import sys
sys.path.append('../register')
from django.urls import path
from . import views
from register.views import logoutUser

# URLConf
urlpatterns = [
    path("", views.index, name="index"),
    path('profile', views.profile, name="profile"),
    path('schedule/', views.schedule, name="schedule"),
    path('messages', views.messages, name="messages"),
    path('about/', views.about, name="about"),
    path('logout/', logoutUser, name='logout'),

]

# start/
