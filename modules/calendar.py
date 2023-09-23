from googleapiclient.discovery import build
from datetime import datetime, timedelta
import random
import string


class Event:
    def __init__(self, summary, description, start_datetime, time_zone='Europe/Madrid'):
        self.summary = summary
        self.description = description
        self.start_datetime = start_datetime
        self.end_datetime = start_datetime + timedelta(minutes=90)
        self.time_zone = time_zone

    def get_event(self):
        event = {
            'summary': self.summary,
            'description': 'description',
            'start': {
                'dateTime': self.start_datetime.strftime('%Y-%m-%dT%H:%M:%S'),
                'timeZone': self.time_zone,
            },
            'end': {
                'dateTime': self.end_datetime.strftime('%Y-%m-%dT%H:%M:%S'),
                'timeZone': self.time_zone,
            },
        }
        return event


def get_events(credentials):
    calendar_id = 'c869dc6f6dee81ae343eced0a4d969e33b95892e88cf588a3eb373129492a640@group.calendar.google.com'
    calendar_service = build('calendar', 'v3', credentials=credentials)
    events = calendar_service.events().list(calendarId=calendar_id).execute()
    return events


def get_event_by_id(credentials, event_id):
    calendar_id = 'c869dc6f6dee81ae343eced0a4d969e33b95892e88cf588a3eb373129492a640@group.calendar.google.com'
    calendar_service = build('calendar', 'v3', credentials=credentials)
    event = calendar_service.events().get(calendarId=calendar_id, eventId=event_id).execute()
    return event


def update_event(credentials, event_id, updated_event):
    calendar_id = 'c869dc6f6dee81ae343eced0a4d969e33b95892e88cf588a3eb373129492a640@group.calendar.google.com'
    calendar_service = build('calendar', 'v3', credentials=credentials)
    event = calendar_service.events().update(calendarId=calendar_id, eventId=event_id,
                                             body=updated_event).execute()
    return event


def create_event(credentials, event):
    calendar_id = 'c869dc6f6dee81ae343eced0a4d969e33b95892e88cf588a3eb373129492a640@group.calendar.google.com'
    calendar_service = build('calendar', 'v3', credentials=credentials)
    event = calendar_service.events().insert(calendarId=calendar_id, body=event).execute()
    return event


def create_event_dry_run(credentials, event):
    class Result:
        def __init__(self, result_id):
            self.id = result_id

    # return Result(''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(25)))
    return Result('6vnjp7464l5oji0ed4cp67hn13')
