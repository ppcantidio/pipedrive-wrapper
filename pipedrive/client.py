import requests

from .activity import Activity
from .deal import Deal
from .deal_field import DealField
from .exceptions import BadRequest, Forbidden, InternalServerError, NotFound, TooManyRequests, Unauthorized
from .person import Person
import logging
from logging import Logger


class Client:
    def __init__(self, token: str, logger: Logger = logging) -> None:
        self.extra_log = None
        self.base_url = "https://api.pipedrive.com/v1"
        self.token = token
        self.headers = {"Accept": "application/json"}
        self.activity = Activity(self)
        self.person = Person(self)
        self.deal = Deal(self)
        self.deal_field = DealField(self)
        self.logger = logger

    def post(self, url_context: str, body: dict):
        url_to_request = self.__generate_url_to_request(url_context)

        self.extra_log = {'request_url': url_to_request, 'http_method': 'POST'}

        body = self.__check_values_of_dict(body)

        response = requests.post(
            url=url_to_request,
            headers=self.headers,
            json=body,
        )

        extra_log_body_content = self.extra_log.copy()
        extra_log_body_content['body'] = body
        self.logger.debug('Body content at extras', extra=extra_log_body_content)

        self.logger.info('Sending request', extra=self.extra_log)

        self.__raise_for_status(response)

        result = self.__parse_response(response)

        return result.get("data")

    def put(self, url_context: str, body: dict):
        url_to_request = self.__generate_url_to_request(url_context)

        self.extra_log = {'request_url': url_to_request, 'http_method': 'PUT'}

        body = self.__check_values_of_dict(body)

        self.logger.info('Sending request', extra=self.extra_log)

        extra_log_body_content = self.extra_log.copy()
        extra_log_body_content['body'] = body
        self.logger.debug('Body content at extras', extra=extra_log_body_content)

        response = requests.put(
            url=url_to_request,
            headers=self.headers,
            json=body,
        )

        self.__raise_for_status(response)

        result = self.__parse_response(response)

        return result.get("data")

    def get(self, url_context: str, params: dict = None):
        url_to_request = self.__generate_url_to_request(url_context)

        self.extra_log = {'request_url': url_to_request, 'http_method': 'GET'}

        if isinstance(params, dict):
            params = self.__check_values_of_dict(params)

        self.extra_log['query_params'] = params

        self.logger.info('Sending request', extra=self.extra_log)

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
        self.extra_log['http_status_code'] = status_code

        if 300 > status_code >= 200:
            self.logger.info('Successful request', extra=self.extra_log)
            return

        self.logger.error(f'Error when performing request, see extra for details', extra=self.extra_log)

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
