from flask import Flask, jsonify, request

import logging

import datetime
import inference_script
import metrics_script

# Initiate flask app
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello world'

@app.route('/predict_api', methods=["GET"])
def chipping():

    

    return 'Prediction result'
    

if __name__ == "__main__":
    app.run()
    # app.run(host='0.0.0.0', port=5000)