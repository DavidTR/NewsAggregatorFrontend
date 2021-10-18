# -*- encoding:utf-8 -*-
"""
                                                  - File description -
------------------------------------------------------------------------------------------------------------------------

"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='login'),
]
