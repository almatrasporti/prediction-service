import numpy as np
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from tensorflow import keras
import pickle
from sklearn.preprocessing import MinMaxScaler

app = Flask(__name__)


@app.route('/', methods=['POST'])
@cross_origin()
def predict():

    content = request.get_json()

    model, scaler = load_data_structures()

    raw_X_input =  content['values']

    X_input = get_scaled_input(raw_X_input, scaler)

    prediction = predict_from_model(X_input, model, scaler)

    return jsonify(
        {
            'values': content['values'],
            'prediction': prediction
        })


def predict_from_model(X_input, model, scaler):
    prediction = scaler.inverse_transform(model.predict(X_input)).tolist()[0][0]
    return prediction


def get_scaled_input(raw_input, scaler):
    X_input = scaler.transform(np.array(raw_input).reshape(-1, 1))
    X_input = np.reshape(X_input, (1, 30, 1))

    return X_input


def load_data_structures():
    model = keras.models.load_model('model')

    with open('model/scaler.pickle', 'rb') as handle:
        scaler = pickle.load(handle)

    return model, scaler


if __name__ == '__main__':
    app.run()
