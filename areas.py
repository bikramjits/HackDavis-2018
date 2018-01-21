"""
Made for Hack Davis 2018 

Building Occupancy Finder for UC Davis 

By 
Bikramjit Singh Kukreja and Gaurav Mulchandani
"""
import json
import numpy as np
import requests
import pprint
from requests.auth import HTTPBasicAuth

#Take in Electricity Data from known buildings on Campus. 

user = "ou\piapihack2018"
passw =  "Go $ave energy, 2018!"
url="https://ucd-piwebapi.ou.ad3.ucdavis.edu/piwebapi/batch"
headers = {'content-type': 'application/json'}

body =  '{  \
  "GetAttributes": {  \
   "Method": "GET",  \
   "Resource": "https://ucd-piwebapi.ou.ad3.ucdavis.edu/piwebapi/attributes/search?databasewebid=F1RDbgZy4oKQ9kiBiZJTW7eugwJztPDnRh5UOIr8WoWgnq3gVVRJTC1BRlxDRUZT&query=Element:%7BTemplate:=%22Building_CEED%22%7D%20Name:=%22Sq.Ft.%22&selectedFields=Items.Links.Value;Items.Path"  \
  },\
   "values": {  \
   "Method": "GET",  \
   "RequestTemplate": {\
     "Resource": "{0}"\
   },\
   "ParentIds": ["GetAttributes"],  \
   "Parameters": ["$.GetAttributes.Content.Items[*].Links.Value"]  \
  }\
}'

req = requests.post(url, data= body,  headers= headers, auth=(user, passw))

json_data = json.loads(req.text)
# print(json_data)

new_var = json_data["values"]

pathz = []
valuez = []

for i in range(134): 
  path = json_data["GetAttributes"]["Content"]["Items"][i]["Path"]
  path = path[33:]
  path = path[:len(path) - 7]
  pathz.append(path)
  value = json_data["values"]["Content"]["Items"][i]["Content"]["Value"]
  if (value == 0): 
        value = 100000
  valuez.append(value)


print(pathz)
print(valuez)

#print(new_var)


# ["Content"]["Items"]

# pprint.pprint(new_var)

# new_arr = []
# for i in range(100): 
# 	new_arr.append(new_var[i]["Content"]["Value"])


#Convert json into python objects (Probably for loop for multiple buildings considering
# the length of the request time). 




#Logic for calculating Occupancy and ranking systems. 

