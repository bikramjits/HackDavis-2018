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
# url = "https://ucd-piwebapi.ou.ad3.ucdavis.edu/piwebapi/attributes/search?databasewebid=F1RDbgZy4oKQ9kiBiZJTW7eugwJztPDnRh5UOIr8WoWgnq3gVVRJTC1BRlxDRUZT&query=Element:{Name:=Electricity}%20Name:=Demand"  

body =  '{  \
  "GetAttributes": {  \
   "Method": "GET",  \
   "Resource": "https://ucd-piwebapi.ou.ad3.ucdavis.edu/piwebapi/attributes/search?databasewebid=F1RDbgZy4oKQ9kiBiZJTW7eugwJztPDnRh5UOIr8WoWgnq3gVVRJTC1BRlxDRUZT&query=Element:{Name:=Electricity}%20Name:=Demand&selectedFields=Items.WebId"  \
  },\
   "values": {  \
   "Method": "GET",  \
   "RequestTemplate": {\
     "Resource": "https://ucd-piwebapi.ou.ad3.ucdavis.edu/piwebapi/streams/{0}/value"\
   },\
   "ParentIds": ["GetAttributes"],  \
   "Parameters": ["$.GetAttributes.Content.Items[*].WebId"]  \
  }\
}'


# print("!")
req = requests.post(url, data= body,  headers= headers, auth=(user, passw))
# print("!")
# print(req.text)

json_data = json.loads(req.text)

new_var = json_data["values"]["Content"]["Items"]

new_arr = []
for i in range(100): 
	# if "Value" in new_var[i]["Content"]: 
	new_arr.append(new_var[i]["Content"]["Value"])


# [0]["Content"]["Value"]

pprint.pprint(new_arr)

#Convert json into python objects (Probably for loop for multiple buildings considering
# the length of the request time). 




#Logic for calculating Occupancy and ranking systems. 

