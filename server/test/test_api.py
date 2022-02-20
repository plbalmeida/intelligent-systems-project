import json
import os
import pytest
import requests
import sys
import urllib

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),'../'))

def test_200():
    '''test if the expected request code 201 is returned.''' 

    url = "http://0.0.0.0:5000/v1/categorize"	
    path = 'test/input.json'
    req = urllib.request.Request(url)
    req.add_header('Content-Type', 'application/json') 
    json_file = open(path)
    json_data = json.load(json_file) 
    json_file.close()
    resp = requests.post(url, json=json_data, headers=req.headers)

    assert resp.status_code == 200


""" @pytest.mark.parametrize('path_400', ('/400/missing_title.json'))
def test_post_expected_400(path_400):
    '''test if the expected request code 400 is returned.''' 
    
    url = "http://0.0.0.0:5000/v1/categorize"	
    path = 'test/data' + path_400
    req = urllib.request.Request(url)
    req.add_header('Content-Type', 'application/json') 
    #json_file = open('test/data/201/test1.json',)
    json_file = open(path)
    json_data = json.load(json_file) 
    json_file.close()
    resp = requests.post(url, json=json_data, headers=req.headers)

    assert resp.status_code == 400
 """