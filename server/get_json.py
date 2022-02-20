import json
import os
import pandas as pd

if __name__ == '__main__':

    input = pd.read_csv(open(os.getenv('TEST_SET_PATH')))
    input_list = input['query'].to_list()
    input_dict = {"products": []}
    input_dict["products"] += [{"query": i} for i in input_list]
    to_json = json.dumps(input_dict)

    with open(os.getenv('JSON_TEST_SET_PATH'), 'w') as f:
        f.write(to_json)
