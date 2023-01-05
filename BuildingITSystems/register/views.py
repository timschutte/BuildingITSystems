from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.template.context_processors import csrf
from crispy_forms.utils import render_crispy_form
from django.contrib.auth import login
from crispy_forms.templatetags.crispy_forms_filters import as_crispy_field


# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
        template = render(request, 'http://127.0.0.1:8000/profile')
        template['Hx-Push'] = '/profile/'
        return template

        ctx = {}
        ctx.update(csrf(request))
        form_html = render_crispy_form(form, context=ctx)
        return HttpResponse(form_html)

    else:
        form = RegisterForm()
    return render(request, "register/register.html", {"form": form})

def check_username(request):
    form = RegisterForm(request.GET)
    context = {
        'field': as_crispy_field(form['username']),
        'valid': not form['username'].errors
    }
    return render(request, 'partials/field.html', context)
