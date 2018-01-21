"""
Made for Hack Davis 2018

Building Occupancy Finder for UC Davis

By
Bikramjit Singh Kukreja and Gaurav Mulchandani
"""
import pandas
from flask import render_template
from flask import Flask
from models import *
import json
import numpy as np
import requests
import pprint
from requests.auth import HTTPBasicAuth
from datascience import *
# import sqlite3
#Take in Electricity Data from known buildings on Campus.

user = "ou\piapihack2018"
passw =  "Go $ave energy, 2018!"
url="https://ucd-piwebapi.ou.ad3.ucdavis.edu/piwebapi/batch"
headers = {'content-type': 'application/json'}

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

req = requests.post(url, data= body,  headers= headers, auth=(user, passw))

json_data = json.loads(req.text)

new_var = json_data["values"]["Content"]["Items"]

new_arr = []
for i in range(100):
	new_arr.append(new_var[i]["Content"]["Value"])

#Convert json into python objects (Probably for loop for multiple buildings considering
# the length of the request time).




#Logic for calculating Occupancy and ranking systems.
Area= Table.read_table('Area_2.csv')
Baseline= Table.read_table('baseline.csv')
Result= Baseline.join('Name', Area)
Buildings = Table.read_table('buildings.csv').with_column('Current', new_arr)
Final= Buildings.join('Name', Result)
Final= Final.with_column('FinalR', (Final.column(1)-Final.column(2))/Final.column(3))
Final=Final.sort(4)
# Final.to_csv('my_table.csv')
# con= MySQLdb.connect()
# df = pandas.read_csv('my_table.csv')
# df.to_sql('Ranking', con= con, if_exists='append', index=False)
# print(Final)

app = Flask(__name__)
@app.route('/')
def index():
  # school_count = School.select().count()
  ranking = Final.column(4)
  return render_template('index.html')
@app.route('/schools/clemente')
def school():
    return render_template('school.html', ranking= ranking)
if __name__ == '__main__':
    app.run(debug=True)
