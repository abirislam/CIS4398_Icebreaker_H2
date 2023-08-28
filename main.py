# curl --request GET \
#     --get "https://courses.ianapplebaum.com/api/syllabus/1" \
#     --header "Authorization: Bearer goPnfrn2AIHUnMmFGhtyfXbRS1zIbdOuJ3OMjl9M" \
#     --header "Content-Type: application/json" \
#     --header "Accept: application/json"

import requests

URL = "https://courses.ianapplebaum.com/api/syllabus/4"

PARAMS = {'Authorization': "Bearer goPnfrn2AIHUnMmFGhtyfXbRS1zIbdOuJ3OMjl9M",
          'Content-Type': "application/json",
          'Accept': "application/json"}


API_KEY = "goPnfrn2AIHUnMmFGhtyfXbRS1zIbdOuJ3OMjl9M"

r = requests.get(url = URL, headers= {'Authorization': "Bearer goPnfrn2AIHUnMmFGhtyfXbRS1zIbdOuJ3OMjl9M",
          'Content-Type': "application/json",
          'Accept': "application/json"})
data = r.json()

print(data)