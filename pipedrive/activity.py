from .util import Util


class Activity:
    def __init__(self, client):
        self._client = client
        self._util = Util()

    def create_activity(
        self,
        due_date: str,
        due_time: str = None,
        duration: str = None,
        deal_id: int = None,
        lead_id: str = None,
        person_id: int = None,
        project_id: int = None,
        org_id: int = None,
        location: str = None,
        public_description: str = None,
        note: str = None,
        subject: str = None,
        type: str = None,
        user_id: int = None,
        participants: list = None,
        busy_flag: bool = None,
        attendees: list = None,
        done: int = None,
    ):
        """
        Create a new activity.

        Args:
            due_date (str): The due date of the activity. Format: YYYY-MM-DD.
            due_time (str): The due time of the activity in UTC. Format: HH:MM.
            duration (str): The duration of the activity. Format: HH:MM.
            deal_id (int): The ID of the deal this activity is associated with.
            lead_id (str): The ID of the lead in the UUID format this activity is associated with.
            person_id (int): The ID of the person this activity is associated with.
            project_id (int): The ID of the project this activity is associated with.
            org_id (int): The ID of the organization this activity is associated with.
            location (str): The address of the activity.
            public_description (str): Additional details about the activity that is synced to your external calendar.
            note (str): The note of the activity (HTML format).
            subject (str): The subject of the activity.
            type (str): The type of the activity.
            user_id (int): The ID of the user whom the activity is assigned to.
            participants (list): List of multiple persons (participants) this activity is associated with.
            busy_flag (bool): Set the activity as 'Busy' or 'Free'.
            attendees (list): The attendees of the activity.
            done (int): Whether the activity is done or not.

        Returns:
            dict: The created activity information as a dictionary.

        Raises:
            ValueError: If there are any validation errors for the fields.

        """
        url_context = "/activities"

        # # Validate fields
        # self._util.validate_due_date(due_date)
        # self._util.validate_due_time(due_time)
        # self._util.validate_duration(duration)
        # if participants is not None:
        #     self._util.validate_participants(participants)
        # if attendees is not None:
        #     self._util.validate_attendees(attendees)
        due_date = due_date.replace("-", "/")
        payload = {
            "due_date": due_date,
            # "due_time": due_time,
            # "duration": duration,
            "deal_id": int(deal_id),
            # "lead_id": lead_id,
            # "person_id": person_id,
            # "project_id": project_id,
            # "org_id": org_id,
            # "location": location,
            # "public_description": public_description,
            # "note": note,
            "subject": subject,
            # "type": type,
            "user_id": user_id,
            # "participants": participants,
            # "busy_flag": busy_flag,
            # "attendees": attendees,
            # "done": done,
        }

        return self._client.post(url_context, payload)

    def update_acitity(self, activity_id: int, done: bool = False):
        url_context = f"/activities/{activity_id}"

        payload = {}
        if done is not None:
            payload['done'] = int(done)

        return self._client._post(url_context, payload)
