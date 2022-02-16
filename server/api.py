import os
import pickle
import pandas as pd
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/v1/categorize', methods=['POST'])
def predict():
    '''API for product category prediction.'''

    json_input = request.json['query']
    query = pd.DataFrame([json_input])
    query.columns = ['query']
    data_engineering = pickle.load(open(os.getenv('DATA_ENGINEERING_PATH'), 'rb'))
    model = pickle.load(open(os.getenv('MODEL_PATH'), 'rb'))
    query_transformed = data_engineering.transform(query)
    prediction = model.predict(query_transformed)
    return jsonify({'categories': prediction})
    