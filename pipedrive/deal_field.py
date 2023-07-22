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
        url_context = f"/deals/{deal_field_id}"

        return self.client._get(url_context)
