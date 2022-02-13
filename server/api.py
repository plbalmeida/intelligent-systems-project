import pandas as pd
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/v1/categorize', methods=['POST'])
def predict():
    '''API for product category prediction.'''

    json_input = request.json
    query = pd.DataFrame(json_input)
    query_transformed = data_engineering.transform(query)
    prediction = model.predict(query_transformed)
    return jsonify({'categories': prediction})

if __name__ == '__main__':
    data_engineering = joblib.load(os.getenv('DATA_ENGINEERING_PATH')) 
    model = joblib.load(os.getenv('MODEL_PATH'))
    app.run(port=5000, debug=True)
