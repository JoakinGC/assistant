from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from datetime import datetime, timedelta

def add_event_to_calendar(summary, description, start_time, end_time):
    credentials = Credentials.from_authorized_user_file('token.json')
    service = build('calendar', 'v3', credentials=credentials)
    event = {
        'summary': summary,
        'description': description,
        'start': {
            'dateTime': start_time.isoformat(),
            'timeZone': 'Europe/Madrid',
        },
        'end': {
            'dateTime': end_time.isoformat(),
            'timeZone': 'Europe/Madrid',
        },
    }
    service.events().insert(calendarId='primary', body=event).execute()

def list_upcoming_events():
    credentials = Credentials.from_authorized_user_file('token.json')
    service = build('calendar', 'v3', credentials=credentials)
    now = datetime.utcnow().isoformat() + 'Z'
    events_result = service.events().list(
        calendarId='primary', timeMin=now,
        maxResults=10, singleEvents=True,
        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No hay próximos eventos.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])
