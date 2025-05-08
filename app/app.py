from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__, static_folder='static', template_folder='templates')
model = joblib.load('model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        features = [np.array(data)]
        prediction = model.predict(features)[0]
        return jsonify({"prediction": int(prediction)})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
