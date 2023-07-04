
import joblib
import pandas as pd

from preprocessing import make_date

from flask import Flask, request, jsonify
app = Flask(__name__)

def process_input(x_json):
    x = pd.DataFrame()
    x['year'] = [x_json['year']]

    if int(x_json['month']) < 10:
        month_value = '0' + str(int(x_json['month']))
    else:
        month_value = str(x_json['month'])
    
    x['month'] = [month_value]

    x['date'] = make_date(x.year, x.month)

    return x


@app.route('/predict', methods=['POST'])
def predict():
    model = joblib.load('../models/model.pkl')

    x_json = request.get_json()

    x = process_input(x_json)

    print(model)
    prediction = model.predict(x)
    prediction = {'prediction': int(prediction)}

    return jsonify(prediction)