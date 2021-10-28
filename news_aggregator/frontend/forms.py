# -*- encoding:utf-8 -*-
"""
                                                  - File description -
------------------------------------------------------------------------------------------------------------------------

"""
from django.forms import CharField, PasswordInput, Form


class LoginForm(Form):

    email = CharField(min_length=6, max_length=25)
    password = CharField(min_length=8, max_length=25, widget=PasswordInput)


class SignupForm(Form):

    name = CharField(min_length=3, max_length=25)
    surname = CharField(min_length=3, max_length=50)
    email = CharField(min_length=6, max_length=25)
    password = CharField(min_length=8, max_length=25, widget=PasswordInput)

