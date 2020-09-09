#!/usr/bin/env python3
from flask import Flask,jsonify,request
import requests
import json

app = Flask(__name__)

Add_URL = '/add'
Retrieve_URL = '/health_check'


@app.route('/')
def rest_api():
    return "This is REST API to Elasticsearch"

#Add
@app.route(Add_URL,methods=['POST'])
def add():
    url = "http://localhost:9200/rbcapp1/serices"
    data = request.data
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url,data = data, headers = headers)
    return response.json()
	
#Health Check
@app.route(Retrieve_URL,methods=['GET'])
def health_check():
    service = request.args.get("service")
    url = "http://localhost:9200/rbcapp1/_search?pretty"
    data = {"size":1, "query": {"match": {"service_name": "%s" % service}}}
    headers = {'Content-Type': 'application/json'}
    response = requests.get(url,data = json.dumps(data), headers = headers)
    return response.json()

if __name__=='__main__':
    app.run(host='0.0.0.0')