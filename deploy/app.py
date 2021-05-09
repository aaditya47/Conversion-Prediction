import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
knn_model = pickle.load(open('knn_model.pkl', 'rb'))
nb_model = pickle.load(open('nb_model.pkl', 'rb'))
svc_model = pickle.load(open('svc_model.pkl', 'rb'))
forest_model = pickle.load(open('forest_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict-knn',methods=['POST'])
def predict_knn():

    int_features = [int(x) for x in request.form.values()]
    print(int_features)
    final_features = [np.array(int_features)]
    print(final_features)
    prediction = knn_model.predict(final_features)

    print(prediction)

    return render_template('index.html', prediction_text='Conversion: {}'.format(prediction))

@app.route('/predict-nb',methods=['POST'])
def predict_nb():

    int_features = [int(x) for x in request.form.values()]
    print(int_features)
    final_features = [np.array(int_features)]
    print(final_features)
    prediction = nb_model.predict(final_features)

    print(prediction)

    return render_template('index.html', prediction_text='Conversion: {}'.format(prediction))

@app.route('/predict-svc',methods=['POST'])
def predict_svc():

    int_features = [int(x) for x in request.form.values()]
    print(int_features)
    final_features = [np.array(int_features)]
    print(final_features)
    prediction = svc_model.predict(final_features)

    print(prediction)

    return render_template('index.html', prediction_text='Conversion: {}'.format(prediction))

@app.route('/results',methods=['POST'])
def results():

    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)