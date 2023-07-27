from .util import Util


class Deal:
    def __init__(self, client) -> None:
        self.client = client
        self._util = Util()

    def create_deal(
        self,
        title: str,
        value: str = None,
        currency: str = None,
        user_id: int = None,
        person_id: int = None,
        org_id: int = None,
        pipeline_id: int = None,
        stage_id: int = None,
        status: str = None,
        expected_close_date: str = None,
        probability: int = None,
        lost_reason: str = None,
        visible_to: str = None,
        add_time: str = None,
        personalized_fields: dict = {},
    ):
        """
        Creates a new deal with the provided information.

        Args:
            title (str): The title or name of the deal.
            value (str, optional): The value of the deal. Default is None.
            currency (str, optional): The currency of the deal. Default is None.
            user_id (int, optional): The ID of the user associated with the deal. Default is None.
            person_id (int, optional): The ID of the person associated with the deal. Default is None.
            org_id (int, optional): The ID of the organization associated with the deal. Default is None.
            pipeline_id (int, optional): The ID of the pipeline associated with the deal. Default is None.
            stage_id (int, optional): The ID of the stage associated with the deal. Default is None.
            status (str, optional): The status of the deal. Default is None.
            expected_close_date (str, optional): The expected close date of the deal. Default is None.
            probability (int, optional): The probability of the deal. Default is None.
            lost_reason (str, optional): The reason for losing the deal. Default is None.
            visible_to (str, optional): The visibility of the deal. Default is None.
            add_time (str, optional): The time when the deal was added. Default is None.

        Returns:
            The created deal object.

        """
        url = "/deals"

        payload = {
            "title": title,
            "value": value,
            "currency": currency,
            "user_id": user_id,
            "person_id": person_id,
            "org_id": org_id,
            "pipeline_id": pipeline_id,
            "stage_id": stage_id,
            "status": status,
            "expected_close_date": expected_close_date,
            "probability": probability,
            "lost_reason": lost_reason,
            "visible_to": visible_to,
            "add_time": add_time,
        }

        payload.update(personalized_fields)

        result = self.client.post(url_context=url, body=payload)

        return result

    def update_deal(
        self,
        deal_id: int,
        title: str = None,
        value: str = None,
        currency: str = None,
        user_id: int = None,
        person_id: int = None,
        org_id: int = None,
        pipeline_id: int = None,
        stage_id: int = None,
        status: str = None,
        expected_close_date: str = None,
        probability: int = None,
        lost_reason: str = None,
        visible_to: str = None,
        add_time: str = None,
    ):
        url_context = f"/deals/{deal_id}"

        payload = {
            "title": title,
            "value": value,
            "currency": currency,
            "user_id": user_id,
            "person_id": person_id,
            "org_id": org_id,
            "pipeline_id": pipeline_id,
            "stage_id": stage_id,
            "status": status,
            "expected_close_date": expected_close_date,
            "probability": probability,
            "lost_reason": lost_reason,
            "visible_to": visible_to,
            "add_time": add_time,
        }

        for key, value in payload:
            if value is None:
                del payload[key]

        result = self.client.put(url_context=url_context,  body=payload)

        return result

    def get_deal_by_id(self, deal_id: int):
        """
        Retrieve a deal by its ID.

        Args:
            deal_id (int): The ID of the deal to retrieve.

        Returns:
            dict: The deal information as a dictionary.

        Raises:
            Exception: If there is an error while retrieving the deal.

        """
        url_context = f"/deals/{deal_id}"

        return self.client.get(url_context)

    def search_deals(
        self,
        term: str,
        exact_match: bool = True,
        person_id: int = None,
        organization_id: int = None,
        status: str = None,
        include_fields: str = None,
        start: int = None,
        limit: int = None,
    ):
        """
        Performs a search for deals based on the provided parameters.

        Args:
            term (str): The search term to filter the deals.
            exact_match (bool, optional): Indicates whether the search should be an exact match. Default is True.
            person_id (int, optional): The ID of the person associated with the deals to be searched. Default is None.
            organization_id (int, optional): The ID of the organization associated with the deals to be searched. Default is None.
            status (str, optional): The status of the deals to be searched. Default is None.
            include_fields (str, optional): The fields to be included in the search response. Default is None.
            start (int, optional): The starting index for paginating the results. Default is None.
            limit (int, optional): The maximum number of results to be returned. Default is None.

        Returns:
            The search result.

        """
        url = f"/deals/search"

        params = {
            "term": term,
            "exact_match": exact_match,
            "person_id": person_id,
            "organization_id": organization_id,
            "status": status,
            "include_fields": include_fields,
            "start": start,
            "limit": limit,
        }

        result = self.client.get(url_context=url, params=params)

        return result

    def get_activities_associated_with_deal(self, deal_id):
        url = f'/deals/{deal_id}/activities'

        result = self.client.get(url_context=url)

        return result
