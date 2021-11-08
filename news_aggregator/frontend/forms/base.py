# -*- encoding:utf-8 -*-
"""
                                                  - File description -
------------------------------------------------------------------------------------------------------------------------

"""
from typing import Union

from django.forms import Form

from frontend.backend_client import BackendClient


class FormBase(Form):
    """Base class for all the forms"""

    def __init__(self, *args, **kwargs):
        super(FormBase, self).__init__(*args, **kwargs)

        # Backend client.
        self._backend_client = BackendClient()

        # Resource name, which will be used in the base methods of this class to automatically perform the request
        # to the backend when needed. If the resource URI depends on dynamic data, this member should include the
        # mandatory placeholders, which will be replaced by the real values before calling. For example:
        # /users/{user_id}/logout. The placeholders follow the built-in format() requirements. Keyword arguments
        # style is recommended: "{first} {last}".format(first='Hello', last='world!')
        self._resource_uri = None

        # Resource's HTTP verb ("GET", "POST", "PUT", ...).
        self._resource_http_verb = None

    def call_backend_service(self, qs_params: dict = None, payload_params: dict = None) -> Union[dict, list]:
        """Calls the backend service and returns the response data"""
        return self._backend_client.call(self._resource_uri, self._resource_http_verb, qs_params=qs_params,
                                         payload_params=payload_params)
