from .util import Util


class DealField:
    def __init__(self, client) -> None:
        self.client = client
        self._util = Util()

    def get_deal_field_by_id(self, deal_field_id: int):
        """
        Retrieve a dealField by its ID.

        Args:
            deal_field_id (int): The ID of the deal to retrieve.

        Returns:
            dict: The dealField information as a dictionary.

        Raises:
            Exception: If there is an error while retrieving the deal.

        """
        url_context = f"/dealsFields/{deal_field_id}"

        return self.client._get(url_context)

    def get_all_deal_fields(self):
        url_context = f"/dealFields"

        return self.client._get(url_context)

    def get_deal_field_by_key(self, deal_field_key: str):
        all_deal_fields = self.get_all_deal_fields()

        for deal_field in all_deal_fields:
            if deal_field.get("key") == deal_field_key:
                return deal_field

    def get_label_of_deal_field_option(self, field_key: str, option_id: int):
        deal_field = self.get_deal_field_by_key(field_key)

        options = deal_field.get("options")

        for option in options:
            if option.get("id") == option_id:
                return option.get("label")
