from flask import Flask
import os
import json
import pickle
import pandas as pd
from flask import request
from functools import reduce 

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello_world():
    return {"message": f"ae {os.getenv('MODEL_PATH')}"}
    

@app.route('/v1/categorize', methods=['POST'])
def post():
    json_file = request.json["products"] #.get('title')
    df = pd.DataFrame().from_dict(json_file)
    cols = df.columns
    return {"message": f"{df.shape}"}
# f_conca = lambda d1, d2: {'title':[d1['title'], d2['title']] , 'query':[d1['query'], d2['query']] , 'concatenated_tags':[d1['concatenated_tags'], d2['concatenated_tags']] }
# reduce(f_conca, data['products'])


