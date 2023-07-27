from .util import Util


class Person:
    def __init__(self, client) -> None:
        self.client = client
        self._util = Util()

    def create_person(
        self,
        name: str,
        phone: str,
        email: str = None,
        owner_id: int = None,
        org_id: int = None,
        visible_to: str = None,
        marketing_status: str = None,
    ):
        """
        Create a new person.

        Args:
            name (str): The name of the person.
            email (str): The email address of the person.
            phone (str): The phone number of the person.
            owner_id (int, optional): The ID of the user who will be marked as the owner of this person.
            org_id (int, optional): The ID of the organization this person will belong to.
            visible_to (str, optional): The visibility of the person.
            marketing_status (str, optional): The marketing status of the person.

        Returns:
            dict: The created person information as a dictionary.

        Raises:
            Exception: If there is an error while creating the person.

        """
        url_context = "/persons"
        body = {
            "name": name,
            "email": [{"value": email}],
            "phone": [{"value": phone}],
            "owner_id": owner_id,
            "org_id": org_id,
            "visible_to": visible_to,
            "marketing_status": marketing_status,
        }

        return self.client.post(url_context, body)

    def search_person(
        self,
        term: str,
        fields: str = None,
        exact_match: bool = False,
        organization_id: int = None,
        include_fields: str = None,
        start: int = 0,
        limit: int = None,
    ):
        """
        Search for persons based on the provided parameters.

        Args:
            term (str): The search term to look for.
            fields (str, optional): The fields to perform the search from.
            exact_match (bool, optional): Indicates whether to perform an exact match against the given term.
            organization_id (int, optional): The ID of the organization to filter persons.
            include_fields (str, optional): Additional fields to include in the results.
            start (int, optional): Pagination start.
            limit (int, optional): Items shown per page.

        Returns:
            dict: The search results as a dictionary.

        Raises:
            Exception: If there is an error while searching for persons.

        """
        url_context = "persons/search"
        params = {
            "term": term,
            "fields": fields,
            "exact_match": exact_match,
            "organization_id": organization_id,
            "include_fields": include_fields,
            "start": start,
            "limit": limit,
        }

        return self.client.get(url_context, params)

    def get_person_by_id(self, person_id: int):
        """
        Retrieve a person by their ID.

        Args:
            person_id (int): The ID of the person to retrieve.

        Returns:
            dict: The person information as a dictionary.

        Raises:
            Exception: If there is an error while retrieving the person.

        """
        url_context = f"/persons/{person_id}"

        return self.client.get(url_context)

    def update_person(
        self,
        person_id: int,
        name: str = None,
        owner_id: int = None,
        org_id: int = None,
        email: list = None,
        phone: list = None,
        visible_to: str = None,
        marketing_status: str = None,
        add_time: str = None,
    ):
        """
        Update a person's information.

        Args:
            person_id (int): The ID of the person to update.
            name (str): The name of the person.
            owner_id (int): The ID of the user who will be marked as the owner of this person.
            org_id (int): The ID of the organization this person will belong to.
            email (list): An email address or a list of email objects related to the person.
            phone (list): A phone number or a list of phone objects related to the person.
            visible_to (str): The visibility of the person.
            marketing_status (str): The marketing status of the person.
            add_time (str): The creation date & time of the person in UTC.

        Returns:
            dict: The updated person information as a dictionary.

        Raises:
            ValueError: If there are any validation errors for the fields.

        """
        url_context = f"/persons/{person_id}"

        # Validate fields
        if email is not None:
            self._util.validate_email(email)
        if phone is not None:
            self._util.validate_phone(phone)
        if visible_to is not None:
            self._util.validate_visible_to(visible_to)
        if marketing_status is not None:
            self._util.validate_marketing_status(marketing_status)

        payload = {
            "name": name,
            "owner_id": owner_id,
            "org_id": org_id,
            "email": email,
            "phone": phone,
            "visible_to": visible_to,
            "marketing_status": marketing_status,
            "add_time": add_time,
        }

        return self.client.put(url_context, payload)
