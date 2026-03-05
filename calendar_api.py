import datetime
from datetime import timezone
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/calendar.events.readonly']

def get_service():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('calendar', 'v3', credentials=creds)
    return service

def get_next_events(quant = 3):
    service = get_service()
    time_now = datetime.datetime.now(timezone.utc).isoformat()

    events_result = service.events().list(
        calendarId='primary', 
        timeMin=time_now,
        maxResults=quant,
        singleEvents=True,
        orderBy='startTime'
    ).execute()

    events = events_result.get('items', [])
    clean_event_list = []

    for event in events:

        event_id = event['id']
        event_name = event.get('summary', 'Evento sem nome')
        
        if 'dateTime' in event['start']:
            time_text = event['start']['dateTime']
            time_obj = datetime.datetime.fromisoformat(time_text)
        else:
            time_text = event['start']['date']

            time_obj = datetime.datetime.strptime(time_text, '%Y-%m-%d').replace(tzinfo=datetime.datetime.now(timezone.utc).astimezone().tzinfo)
            
        clean_event_list.append({
            'id': event_id,
            'nome': event_name,
            'horario': time_obj
        })

    return clean_event_list


if __name__ == '__main__':
    eventos = get_next_events(3)
    
    agora_local = datetime.datetime.now(timezone.utc).astimezone()
    print(f"Hora atual: {agora_local.strftime('%H:%M:%S')}\n")
    
    for ev in eventos:
        diferenca_minutos = (ev['horario'] - agora_local).total_seconds() / 60
        print(f"[{ev['nome']}]")
        print(f"  Horário: {ev['horario'].strftime('%d/%m/%Y %H:%M')}")
        print(f"  Faltam/Passaram: {diferenca_minutos:.1f} minutos\n")