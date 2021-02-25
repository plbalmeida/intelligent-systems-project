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

def test_post_expected_201():
    
    url = "http://0.0.0.0:5000/v1/categorize"
    req = urllib.request.Request(url)
    req.add_header('Content-Type', 'application/json') 
    json_file = open('test/data/test1.json',)
    json_data = json.load(json_file) 
    json_file.close()
    resp = requests.post(url, json=json_data, headers=req.headers)

    assert resp.status_code == 201

if __name__ == '__main__':
    #print(type(requestPredictor(df1).predict))
    #urlib.request.Request()

    #data = urllib.parse.urlencode(test_1)
    #data = data.encode('ascii')
    #print(data)
    url = "http://0.0.0.0:5000/v1/categorize"
    #response = urllib.request.urlopen(url, data)
    #print(response)
    #print(response.info()) 
    #myjson = open('test1.json',)

    #headers = {"Content-Type":"application/json"} 

    #x = requests.post(url,headers=headers ,data = test_1)
    #print(x)
    host = url
    # host += '/invoiceHistory/'
    req = urllib.request.Request(host)

    req.add_header('Content-Type', 'application/json') 
    r = requests.post(host, json=test_1, headers=req.headers)
    print(r.status_code)
    content = json.loads(r.content)
    print(content)
