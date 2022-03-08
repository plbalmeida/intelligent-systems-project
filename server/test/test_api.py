import json
import os
import requests
import sys
import urllib

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),'../'))

def response_200():
    '''test if the expected request code 201 is returned.''' 

    url = 'http://0.0.0.0:5000/v1/categorize'	
    path = 'test/test_products.json'
    req = urllib.request.Request(url)
    req.add_header('Content-Type', 'application/json') 
    json_file = open(path)
    json_data = json.load(json_file) 
    json_file.close()
    resp = requests.post(url, json=json_data, headers=req.headers)

    assert resp.status_code == 200
