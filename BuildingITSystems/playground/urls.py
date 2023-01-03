from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path("", views.index, name="index"),
    path('profile', views.profile, name="profile"),
    path('schedule/', views.schedule, name="schedule"),
    path('messages', views.messages, name="messages"),
    path('about/', views.about, name="about"),
    path('test', views.test, name="test"),
    path('footer', views.footer, name="footer"),
 

]

# start/
