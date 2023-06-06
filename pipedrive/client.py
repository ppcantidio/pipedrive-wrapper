import requests

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
        response.raise_for_status()

        result = self.__parse_response(response)

        return result.get("data")

    def _put(self, url_context, body):
        url_to_request = self.__generate_url_to_request(url_context)
        headers = self.__generate_headers()

        body = self.__check_values_of_dict(body)

        response = requests.put(url=url_to_request, headers=headers, json=body)
        response.raise_for_status()

        result = self.__parse_response(response)

        return result.get("data")

    def _get(self, url_context, params=None):
        url_to_request = self.__generate_url_to_request(url_context)
        headers = self.__generate_headers()

        if isinstance(params, dict):
            params = self.__check_values_of_dict(params)

        response = requests.get(url=url_to_request, headers=headers, params=params)
        response.raise_for_status()

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
