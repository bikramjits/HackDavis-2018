"""
Made for Hack Davis 2018 

Building Occupancy Finder for UC Davis 

By 
Bikramjit Singh Kukreja and Gaurav Mulchandani
"""
import json
import requests
from requests.auth import HTTPBasicAuth

#Take in Electricity Data from known buildings on Campus. 
user = "ou\piapihack2018"
passw =  "Go $ave energy, 2018!"
url = "https://ucd-piwebapi.ou.ad3.ucdavis.edu/piwebapi/attributes/search?databasewebid=F1RDbgZy4oKQ9kiBiZJTW7eugwJztPDnRh5UOIr8WoWgnq3gVVRJTC1BRlxDRUZT&query=%20Element:{Name:=Electricity}%20Name:=Demand"  

# url = " {  
#   "GetAttributes": {  
#    "Method": "GET",  
#    "Resource": "https://ucd-piwebapi.ou.ad3.ucdavis.edu/piwebapi/attributes/search?databasewebid=F1RDbgZy4oKQ9kiBiZJTW7eugwJztPDnRh5UOIr8WoWgnq3gVVRJTC1BRlxDRUZT&query=%20Element:{Name:=Electricity}%20Name:=Demand"  
#   },  
#   "values": {  
#    "Method": "GET",  
#    "RequestTemplate": {
#      "Resource": "https://ucd-piwebapi.ou.ad3.ucdavis.edu/piwebapi/streams/{0}/interpolated"
#    },
#    "ParentIds": ["GetAttributes"],  
#    "Parameters": ["$.GetAttributes.Content.Items[*].WebId"]  
#   }  
# }  "

req = requests.get(url, auth=HTTPBasicAuth(user, passw))

print(req)

json_data = json.loads(req.text)

new_var = json_data["Items"][0]["Value"]
# ["Items"][0]["Value"]

print(new_var)



#Convert json into python objects (Probably for loop for multiple buildings considering
# the length of the request time). 




#Logic for calculating Occupancy and ranking systems. 

