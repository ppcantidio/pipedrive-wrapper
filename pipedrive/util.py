import re


class Util:
    def __init__(self) -> None:
        pass

    def check_values_of_dict(self, params: dict):
        return {key: value for key, value in params.items() if value is not None}

    # Validation methods
    def validate_email(self, email):
        if not isinstance(email, list):
            raise ValueError("Email must be a list of email objects.")

        for email_obj in email:
            if not isinstance(email_obj, dict) or "value" not in email_obj:
                raise ValueError("Email object must be a dictionary with 'value' field.")

            email_value = email_obj["value"]
            if not isinstance(email_value, str) or not re.match(r"[^@]+@[^@]+\.[^@]+", email_value):
                raise ValueError("Invalid email address.")

    def validate_phone(self, phone):
        if not isinstance(phone, list):
            raise ValueError("Phone must be a list of phone objects.")

        for phone_obj in phone:
            if not isinstance(phone_obj, dict) or "value" not in phone_obj:
                raise ValueError("Phone object must be a dictionary with 'value' field.")

            phone_value = phone_obj["value"]
            if not isinstance(phone_value, str) or not re.match(r"\d+", phone_value):
                raise ValueError("Invalid phone number.")

    def validate_visible_to(self, visible_to):
        valid_values = ["1", "3", "5", "7"]
        if visible_to not in valid_values:
            raise ValueError("Invalid value for visible_to. Allowed values are: 1, 3, 5, 7.")

    def validate_marketing_status(self, marketing_status):
        valid_values = ["no_consent", "unsubscribed", "subscribed", "archived"]
        if marketing_status not in valid_values:
            raise ValueError(
                "Invalid value for marketing_status. Allowed values are: no_consent, unsubscribed, subscribed, archived."
            )
