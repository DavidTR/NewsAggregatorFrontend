# -*- encoding:utf-8 -*-
"""
                                                  - File description -
------------------------------------------------------------------------------------------------------------------------

"""
from typing import Union

from django import forms as django_forms

from .base import FormBase


class RSSFeedsNewsForm(FormBase):

    user_id = django_forms.IntegerField(widget=django_forms.HiddenInput(), initial=1)

    def __init__(self, *args, **kwargs):
        super(RSSFeedsNewsForm, self).__init__(*args, **kwargs)
        self._resource_uri = "/users/{user_id}/subscriptions"
        self._resource_http_verb = "GET"

    def call_backend_service(self, qs_params: dict = None, payload_params: dict = None) -> Union[dict, list]:
        self._resource_uri = self._resource_uri.format(**self.cleaned_data)
        return super(RSSFeedsNewsForm, self).call_backend_service(qs_params=None, payload_params=None)
