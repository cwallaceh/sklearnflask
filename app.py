# Local imports
import pickle
import sys
import logging
import gzip
import datetime

# Third part imports
from flask import Flask, request, jsonify
import pandas as pd


app = Flask(__name__)


model_file = 'model_binary.dat.gz'


@app.route('/predict', methods=['POST'])
def predict():
    """Return model prediction"""
    result = {}

    payload = request.json
    result["payload"] = payload
    df = pd.DataFrame(payload)

    result["name"] = "titanic_test_model"
    result["version"] = "v1.0.0"

    prediction = model.predict_proba(df)
    result['prediction'] = round(prediction[0][0], 2)
    result['timestamp'] = datetime.datetime.now()

    return result


@app.route('/info', methods=['GET'])
def info():
    """Return model information, version, how to call"""
    result = {}

    result["name"] = "titanic_test_model"
    result["version"] = "v1.0.0"

    return result


if __name__ == '__main__':
    try:
        port = int(sys.argv[1])
    except Exception as e:
        port = 8080

    file = gzip.open(model_file, "rb")
    model = pickle.load(file)

    app.run(host='0.0.0.0', port=port, debug=False)
