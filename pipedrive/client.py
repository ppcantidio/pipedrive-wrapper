import requests

from .exceptions import BadRequest, Forbidden, InternalServerError, NotFound, TooManyRequests, Unauthorized
from .util import Util


class Client:
    def __init__(self, token: str) -> None:
        self.base_url = "https://api.pipedrive.com/v1"
        self.token = token
        self._utl = Util()

    def _post(self, url_context, body):
        url_to_request = self.__generate_url_to_request(url_context)
        headers = self.__generate_headers()

        body = self.__check_values_of_dict(body)

        response = requests.post(url=url_to_request, headers=headers, json=body)
        self.__raise_for_status(response)

        result = self.__parse_response(response)

        return result.get("data")

    def _put(self, url_context, body):
        url_to_request = self.__generate_url_to_request(url_context)
        headers = self.__generate_headers()

        body = self.__check_values_of_dict(body)

        response = requests.put(url=url_to_request, headers=headers, json=body)
        self.__raise_for_status(response)

        result = self.__parse_response(response)

        return result.get("data")

    def _get(self, url_context, params=None):
        url_to_request = self.__generate_url_to_request(url_context)
        headers = self.__generate_headers()

        if isinstance(params, dict):
            params = self.__check_values_of_dict(params)

        response = requests.get(url=url_to_request, headers=headers, params=params)
        self.__raise_for_status(response)

        result = self.__parse_response(response)

        return result.get("data")

    def __generate_headers(self):
        headers = {"Accept": "application/json"}
        return headers

    def __generate_url_to_request(self, url_context: str):
        url_to_request = f"{self.base_url}/{url_context}"
        return url_to_request

    def __parse_response(self, response: requests.Response):
        return response.json()

    def __check_values_of_dict(self, params: dict):
        return {key: value for key, value in params.items() if value is not None}

    def __raise_for_status(self, response):
        status_code = response.status_code

        if 300 > status_code >= 200:
            return

        if status_code == 400:
            raise BadRequest()

        if status_code == 401:
            raise Unauthorized()

        if status_code == 403:
            raise Forbidden()

        if status_code == 404:
            raise NotFound()

        if status_code == 429:
            raise TooManyRequests()

        if status_code >= 500:
            raise InternalServerError()
