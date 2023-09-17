from googleapiclient.discovery import build


def get_events(credentials):
    calendar_id = 'c869dc6f6dee81ae343eced0a4d969e33b95892e88cf588a3eb373129492a640@group.calendar.google.com'
    calendar_service = build('calendar', 'v3', credentials=credentials)
    events = calendar_service.events().list(calendarId=calendar_id).execute()
    return events
