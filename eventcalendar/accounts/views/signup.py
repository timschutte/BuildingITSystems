# /*************************************************************** 
# *Title: Event Calendar 
# *Author: sajib1066 
# *Date: 5 July 2020 
# *Code version: V79 
# *Availability: https://github.com/sajib1066/event-calendar (Accessed 14 December 2022) 
# ****************************************************************/

from django.views.generic import View
from django.shortcuts import render, redirect

from accounts.forms import SignUpForm


class SignUpView(View):
    """ User registration view """

    template_name = "accounts/signup.html"
    form_class = SignUpForm

    def get(self, request, *args, **kwargs):
        forms = self.form_class()
        context = {"form": forms}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        forms = self.form_class(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect("accounts:signin")
        context = {"form": forms}
        return render(request, self.template_name, context)
