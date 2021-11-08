# -*- encoding:utf-8 -*-
"""
                                                  - File description -
------------------------------------------------------------------------------------------------------------------------

"""
from typing import Union

import requests

from cfg.config import settings


class BackendClient:
    """Implements the logic that allows establishing communications with a backend"""

    def __init__(self):

        # Load backend config settings.
        backend_config = settings.BACKEND

        # Base host URL.
        self._host_base_url = "".join([backend_config["HOST_BASE_URL"], backend_config["CURRENT_VERSION"]])

    def call(self, resource_uri: str, resource_http_verb: str,  qs_params: dict = None,
             payload_params: dict = None) -> Union[dict, list]:
        """Makes a request to the backend and returns the response content as JSON"""
        request_url = "".join([self._host_base_url, resource_uri])

        response = requests.request(resource_http_verb, request_url, params=qs_params, data=payload_params)

        # TODO: Cambiar el comportamiento de este método para tratar mejor los códigos no 200. Por ahora hace un raise.
        response.raise_for_status()

        # TODO: Si este método genera una excepción, hay que tratarla para que no llegue al frontal como error no
        #  controlado.
        return response.json()


