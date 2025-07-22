from flask import Flask, render_template, request
import joblib
import pickle
import numpy as np

# Load the trained model
model = joblib.load(open("model/heart_failure_model.pkl", "rb"))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [float(x) for x in request.form.values()]
        final_features = np.array(features).reshape(1, -1)
        prediction = model.predict(final_features)
        output = 'Patient is at risk of Heart Failure' if prediction[0] == 1 else 'Patient is NOT at risk of Heart Failure'
        return render_template('index.html', prediction_text=output)
    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
