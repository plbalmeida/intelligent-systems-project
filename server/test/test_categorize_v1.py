import os
import sys
import pandas as pd
import pytest
import urllib
import requests
import json

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),'../'))

from request_predictor import requestPredictor



test_1 = {"products": [{"title": "Lembrancinha 15 anos - Lembrancinha de 15 anos", "query": "lembrancinhas de 15 anos", "concatenated_tags": "15 anos"}, {"title": "Trio de Nichos Prateleira", "query": "prateleira", "concatenated_tags": "prateleiras decoracao gaveteiros nichos prateleiras nichos"}]}

test_2 = {"products": [{"titl": "Lembrancinha 15 anos - Lembrancinha de 15 anos", "query": "lembrancinhas de 15 anos", "concatenated_tags": "15 anos"}, {"title": "Trio de Nichos Prateleira", "query": "prateleira", "concatenated_tags": "prateleiras decoracao gaveteiros nichos prateleiras nichos"}]}

test_3 = {"products": [{"title": "Lembrancinha 15 anos - Lembrancinha de 15 anos", "query": "lembrancinhas de 15 anos", "concatenated_tags": "15 anos"}, {"title": "Trio de Nichos Prateleira", "query": "prateleira", "concatenated_tags": "prateleiras decoracao gaveteiros nichos prateleiras nichos"}]}

test_4 = {"products": [{"title": "Lembrancinha 15 anos - Lembrancinha de 15 anos", "query": "lembrancinhas de 15 anos", "concatenated_tags": "15 anos"}, {"title": "Trio de Nichos Prateleira", "query": "prateleira", "concatenated_tags": "prateleiras decoracao gaveteiros nichos prateleiras nichos"}]}

df1 = pd.DataFrame().from_dict(test_1['products']) 
df2 = pd.DataFrame().from_dict(test_1['products']) 

@pytest.mark.parametrize('path_201', (
    '/201/expected_items_in_product.json',
    '/201/extra_item_in_product.json'))
def test_post_expected_201(path_201):
    
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

if __name__ == '__main__':
    url = "http://0.0.0.0:5000/v1/categorize"
    host = url
    req = urllib.request.Request(host)

    req.add_header('Content-Type', 'application/json') 
    r = requests.post(host, json=test_1, headers=req.headers)
    print(r.status_code)
    content = json.loads(r.content)
    print(content)
