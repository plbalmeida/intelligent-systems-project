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

    json_file = request.json["products"] #.get('title')
    df = pd.DataFrame().from_dict(json_file)
    req_predictor = requestPredictor(df)

    return req_predictor.predict
