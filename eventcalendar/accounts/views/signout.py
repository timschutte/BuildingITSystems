# /*************************************************************** 
# *Title: Event Calendar 
# *Author: sajib1066 
# *Date: 5 July 2020 
# *Code version: V79 
# *Availability: https://github.com/sajib1066/event-calendar (Accessed 14 December 2022) 
# ****************************************************************/

from django.shortcuts import redirect
from django.contrib.auth import logout


def signout(request):
    logout(request)
    return redirect("accounts:signin")
