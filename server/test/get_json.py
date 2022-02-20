import json
import os
import pandas as pd
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),'../'))

if __name__ == '__main__':

    input = pd.read_csv('test_products.csv')
    input_list = input['query'].to_list()
    input_dict = {"products": []}
    input_dict["products"] += [{"query": i} for i in input_list]
    to_json = json.dumps(input_dict)

    with open('test_products.json', 'w') as f:
        f.write(to_json)
