import requests
import json
from ms_graph import generate_access_token
from datetime import datetime, timedelta

URL = "https://courses.ianapplebaum.com/api/syllabus/4"

PARAMS = {'Authorization': "Bearer goPnfrn2AIHUnMmFGhtyfXbRS1zIbdOuJ3OMjl9M",
          'Content-Type': "application/json",
          'Accept': "application/json"}


API_KEY = "goPnfrn2AIHUnMmFGhtyfXbRS1zIbdOuJ3OMjl9M"

r = requests.get(url = URL, headers= PARAMS)
data = r.json()


with open('Important Dates.csv', 'w', encoding='utf-8') as f:
    f.write("Event Name,Description,Date\n")
    for x in range(len(data["events"])):
        f.write(str(data["events"][x]['event_name']))
        f.write(",")
        f.write("\"" + str(data["events"][x]['event_description']) + "\"")
        f.write(",")
        f.write(str(data["events"][x]['event_date']))
        f.write("\n")
    

msalHeaders = {
    'Authorization': f'Bearer [ACCESS TOKEN HERE]', 
    'Content-Type': "application/json",
      'Accept': "application/json"
}
for x in range(len(data["events"])):
    event_data = {
        'subject': str(data["events"][x]['event_name']),

        'body': {
            'content': str(data["events"][x]['event_description']),
            'contentType': 'text'
        },

        'start': {
            'dateTime':(datetime.strptime(str(data["events"][x]['event_date']),'%Y-%m-%d')).isoformat(),
            'timeZone': 'America/New_York'
        },
        'end': {
            'dateTime': (datetime.strptime(str(data["events"][x]['event_date']),'%Y-%m-%d') + timedelta(hours=24)).isoformat(),
            'timeZone': 'America/New_York'
        },
    }

    msalResponse = requests.post(
        'https://graph.microsoft.com/v1.0/me/events',
        headers=msalHeaders,
        data=json.dumps(event_data)
    )

    if msalResponse.status_code == 201:
        print('Event created successfully')
    else:
        print('Failed to create event:', msalResponse.text)
