import os
import json
import pickle
import pandas as pd
import numpy as np
from flask import Flask, request

app = Flask(__name__)

@app.route('/v1/categorize', methods=['POST'])
def post():
    try:
        json_ = request.json['products']
        
