from flask import Flask, Response, request, request_finished
import pandas as pd
import os
from flask_cors import CORS
import pickle

app = Flask(__name__)
CORS(app)


@app.route("/")
def get_index():
    return {'hello': 'world'}


@app.route("/hello_world")
def get_hello_world():
    return "<p>Hello, Deutschland!</p>"


@app.route("/training_data")
def get_training_data():
    data = pd.read_csv('data/auto-mpg-training-data.csv', sep=";")
    return Response(data.to_json(), mimetype='application/json')


@app.route("/predict_data")
def get_predict():
    zylinder = request.args.get('zylinder')
    ps = request.args.get('ps')
    gewicht = request.args.get('gewicht')
    beschleunigung = request.args.get('beschleunigung')
    baujahr = request.args.get('baujahr')

    file_to_open = open("data/models/baummethoden_lr.pickle", "rb")
    trained_model = pickle.load(file_to_open)
    file_to_open.close()

    prediction = trained_model.predict(
        [[zylinder, ps, gewicht, beschleunigung, baujahr]])
    print(prediction)
    return {'result': prediction[0]}


