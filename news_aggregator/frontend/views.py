from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

# Create your views here.
# This weird import expression is the only way I found to make "manage.py makemigrations" not freak out about not
# finding the file.
from .forms.landing import LoginForm
from .forms.rss_feeds import RSSFeedsNewsForm


def index(request: WSGIRequest):
    if request.method == "POST":
        login_form = LoginForm(request.POST)
    else:
        login_form = LoginForm()

    return render(request, 'index.html', context={"login_form": login_form})


def news_list(request: WSGIRequest):
    rss_news = {}

    if request.method == "POST":
        form = RSSFeedsNewsForm(request.POST)

        if form.is_valid():
            rss_news = form.call_backend_service(qs_params=form.cleaned_data)

    else:
        form = RSSFeedsNewsForm()

    return render(request, 'news_list.html', {"rss_news": rss_news, "form": form})
