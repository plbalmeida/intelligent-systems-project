import os
import pickle
import pandas as pd
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/v1/categorize', methods=['POST'])
def predict():
    '''API for product category prediction.'''

    json_input = request.json['query']
    query = pd.DataFrame(json_input)
    data_engineering = pickle.load(os.getenv('DATA_ENGINEERING_PATH'))
    model = pickle.load(os.getenv('MODEL_PATH'))
    query_transformed = data_engineering.transform(query)
    prediction = model.predict(query_transformed)
    return jsonify({'categories': prediction})
    