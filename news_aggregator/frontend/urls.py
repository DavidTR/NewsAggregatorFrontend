# -*- encoding:utf-8 -*-
"""
                                                  - File description -
------------------------------------------------------------------------------------------------------------------------

"""
from django.urls import path

# This weird import expression is the only way I found to make "manage.py makemigrations" not freak out about not
# finding the file.
from . import views

urlpatterns = [
    # path('', views.index, name='login'),
    path('', views.news_list, name="news_list")
]
