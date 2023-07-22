import requests

from .activity import Activity
from .deal import Deal
from .deal_field import DealField
from .exceptions import BadRequest, Forbidden, InternalServerError, NotFound, TooManyRequests, Unauthorized
from .person import Person


class Client:
    def __init__(self, token: str) -> None:
        self.base_url = "https://api.pipedrive.com/v1"
        self.token = token
        self.headers = {"Accept": "application/json"}
        self.activity = Activity(self)
        self.person = Person(self)
        self.deal = Deal(self)
        self.deal_field = DealField(self)

    def _post(self, url_context: str, body: dict):
        url_to_request = self.__generate_url_to_request(url_context)

        body = self.__check_values_of_dict(body)

        response = requests.post(
            url=url_to_request,
            headers=self.headers,
            json=body,
        )

        self.__raise_for_status(response)

        result = self.__parse_response(response)

        return result.get("data")

    def _put(self, url_context: str, body: dict):
        url_to_request = self.__generate_url_to_request(url_context)

        body = self.__check_values_of_dict(body)

        response = requests.put(
            url=url_to_request,
            headers=self.headers,
            json=body,
        )

        self.__raise_for_status(response)

        result = self.__parse_response(response)

        return result.get("data")

    def _get(self, url_context: str, params: dict = None):
        url_to_request = self.__generate_url_to_request(url_context)

        if isinstance(params, dict):
            params = self.__check_values_of_dict(params)

        response = requests.get(
            url=url_to_request,
            headers=self.headers,
            params=params,
        )

        self.__raise_for_status(response)

        result = self.__parse_response(response)

        return result.get("data")

    def __generate_url_to_request(self, url_context: str):
        url_to_request = f"{self.base_url}{url_context}?api_token={self.token}"
        return url_to_request

    def __parse_response(self, response: requests.Response):
        return response.json()

    def __check_values_of_dict(self, params: dict):
        return {key: value for key, value in params.items() if value is not None}

    def __raise_for_status(self, response: requests.Response):
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
