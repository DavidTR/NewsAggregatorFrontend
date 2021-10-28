from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

# Create your views here.
# This weird import expression is the only way I found to make "manage.py makemigrations" not freak out about not
# finding the file.
from . import forms


def index(request: WSGIRequest):
    if request.method == "POST":
        login_form = forms.LoginForm(request.POST)
    else:
        login_form = forms.LoginForm()

    return render(request, 'index.html', context={"login_form": login_form})
