from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load('water_quality_model_ada.joblib')

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        features = [float(request.form['ph']),
                    float(request.form['Hardness']),
                    float(request.form['Solids']),
                    float(request.form['Chloramines']),
                    float(request.form['Sulfate']),
                    float(request.form['Conductivity']),
                    float(request.form['Organic_carbon']),
                    float(request.form['Trihalomethanes']),
                    float(request.form['Turbidity']),
                    ]
        prediction1 = model.predict([features])[0]
        if prediction1 == 0:
            prediction = "Not Potable"
            url = "static/images/non_potable.png"
        else:
            prediction = "Potable"
            url = "static/images/potable.svg"

        return render_template('result.html', prediction=prediction, prediction1=prediction1, url=url)

if __name__ == '__main__':
    app.run(debug=True)
