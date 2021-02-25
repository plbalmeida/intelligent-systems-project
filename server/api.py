from flask import Flask
import os
import json
import pickle
import pandas as pd
import numpy as np

from flask import request

from request_predictor import requestPredictor


app = Flask(__name__)

@app.route('/v1/categorize', methods=['POST'])
def post():

    try:
        json_file_list = request.json["products"] #.get('title')
    
    except Exception as e:
        return {'api return': str(e)}, 400
    
    for dict_ in json_file_list:
        try:
            params = set(dict_.keys())
        except Exception as e:
            return {'Error:': str(e)}, 400

        if 'title' not in params or 'query' not in params or 'concatenated_tags' not in params:
            return {'Error':f"bad request in {dict_}"}, 400

    try:
        df = pd.DataFrame().from_dict(json_file_list)

    except Exception as e:
        return {'Error': str(e)}, 400

    req_predictor = requestPredictor(df)

    return req_predictor.predict
