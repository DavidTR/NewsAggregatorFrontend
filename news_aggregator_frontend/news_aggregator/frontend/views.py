from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

# Create your views here.
from news_aggregator_frontend.news_aggregator.frontend.forms import LoginForm, SignupForm


def index(request: WSGIRequest):
    if request.method == "POST":
        login_form = LoginForm(request.POST)
    else:
        login_form = LoginForm()

    return render(request, 'index.html', context={"login_form": login_form})
