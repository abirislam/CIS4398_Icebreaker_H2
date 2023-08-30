import requests
import json

URL = "https://courses.ianapplebaum.com/api/syllabus/4"

PARAMS = {'Authorization': "Bearer goPnfrn2AIHUnMmFGhtyfXbRS1zIbdOuJ3OMjl9M",
          'Content-Type': "application/json",
          'Accept': "application/json"}


API_KEY = "goPnfrn2AIHUnMmFGhtyfXbRS1zIbdOuJ3OMjl9M"

r = requests.get(url = URL, headers= {'Authorization': "Bearer goPnfrn2AIHUnMmFGhtyfXbRS1zIbdOuJ3OMjl9M",
          'Content-Type': "application/json",
          'Accept': "application/json"})
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
    

