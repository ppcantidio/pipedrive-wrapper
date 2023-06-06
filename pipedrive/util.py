import re


class Util:
    def __init__(self) -> None:
        pass

    def check_values_of_dict(self, params: dict):
        return {key: value for key, value in params.items() if value is not None}

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

    def validate_due_date(self, due_date):
        if not re.match(r"^\d{4}-\d{2}-\d{2}$", due_date):
            raise ValueError("Invalid due_date format. Expected format: YYYY-MM-DD")

    def validate_due_time(self, due_time):
        if not re.match(r"^\d{2}:\d{2}$", due_time):
            raise ValueError("Invalid due_time format. Expected format: HH:MM")

    def validate_duration(self, duration):
        if not re.match(r"^\d{2}:\d{2}$", duration):
            raise ValueError("Invalid duration format. Expected format: HH:MM")

    def validate_participants(self, participants):
        if not isinstance(participants, list):
            raise ValueError("participants must be a list")
        for participant in participants:
            if not isinstance(participant, dict) or "person_id" not in participant:
                raise ValueError(
                    "Invalid participant format. Expected format: [{'person_id': 1, 'primary_flag': True}]"
                )

    def validate_attendees(self, attendees):
        if not isinstance(attendees, list):
            raise ValueError("attendees must be a list")
        for attendee in attendees:
            if not isinstance(attendee, dict) or "email_address" not in attendee:
                raise ValueError("Invalid attendee format. Expected format: [{'email_address': 'mail@example.org'}]")
