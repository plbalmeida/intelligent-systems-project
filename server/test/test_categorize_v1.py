import os
import sys
import pytest
import urllib
import requests
import json
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),'../'))
from request_predictor import requestPredictor


@pytest.mark.parametrize('path_201', (
    '/201/expected_items_in_product.json',
    '/201/extra_item_in_product.json'))
def test_post_expected_201(path_201):
    '''
    test if the expected request code 201 is returned.
    ''' 

    url = "http://0.0.0.0:5000/v1/categorize"	
    path = 'test/data' + path_201
    req = urllib.request.Request(url)
    req.add_header('Content-Type', 'application/json') 
    json_file = open(path)
    json_data = json.load(json_file) 
    json_file.close()
    resp = requests.post(url, json=json_data, headers=req.headers)

    assert resp.status_code == 201


@pytest.mark.parametrize('path_400', (
    '/400/missing_title.json',
    '/400/missing_query.json',
    '/400/missing_concatenated_tags.json',
    '/400/missing_products.json',
    '/400/wrong_variable_name_concatenated_tags.json',
    '/400/wrong_variable_name_query.json',
    '/400/wrong_variable_name_title.json',
    '/400/random.json'
    ))
def test_post_expected_400(path_400):
    '''
    test if the expected request code 400 is returned.
    ''' 
    
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
