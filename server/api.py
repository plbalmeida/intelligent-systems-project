import json
import os
import pickle
import pandas as pd
from flask import Flask, request

app = Flask(__name__)

@app.route('/v1/categorize', methods=['POST'])
def predict():
    '''API for product category prediction.'''

    json_input = request.json['products']
    query = pd.DataFrame(json_input)
    data_engineering = pickle.load(open(os.getenv('FEATURE_ENGINEERING_PATH'), 'rb'))
    model = pickle.load(open(os.getenv('MODEL_PATH'), 'rb'))
    query_transformed = data_engineering.transform(query['query'])
    prediction = model.predict(query_transformed)
    return json.dumps({"categories": list(prediction)}), 400
  