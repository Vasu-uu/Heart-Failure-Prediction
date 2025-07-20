from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)
with open('scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

@app.route('/')
def home():
    return render_template('index.html', form_data={})

@app.route('/predict', methods=['POST'])
def predict():
    features = [float(x) for x in request.form.values()]
    final_features = np.array(features).reshape(1, -1)
    scaled_features = scaler.transform(final_features)
    
    prediction = model.predict(scaled_features)
    
    if prediction[0] == 1:
        output = "Prediction: High risk of heart failure event."
        risk_class = 'high-risk'
    else:
        output = "Prediction: Low risk of heart failure event."
        risk_class = 'low-risk'

    return render_template('index.html', 
                           prediction_text=output,
                           risk_class=risk_class, 
                           form_data=request.form)

if __name__ == "__main__":
    app.run(debug=True)