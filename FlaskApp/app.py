from flask import Flask, render_template, request
import pickle
import pandas as pd
import numpy as np
import os

app = Flask(__name__)

# Load your trained ML model
model = pickle.load(open('gwp.pkl', 'rb'))

# Define the exact column names used during training
FEATURE_COLUMNS = [
    'no_of_workers', 'no_of_style_change', 'targeted_productivity',
    'smv', 'wip', 'over_time', 'incentive', 'idle_time', 'idle_men'
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Collect input from form
        data = {
            'no_of_workers': float(request.form['no_of_workers']),
            'no_of_style_change': float(request.form['no_of_style_change']),
            'targeted_productivity': float(request.form['targeted_productivity']),
            'smv': float(request.form['smv']),
            'wip': float(request.form['wip']),
            'over_time': float(request.form['over_time']),
            'incentive': float(request.form['incentive']),
            'idle_time': float(request.form['idle_time']),
            'idle_men': float(request.form['idle_men'])
        }

        # Convert to DataFrame with correct column names
        final_input = pd.DataFrame([data], columns=FEATURE_COLUMNS)

        # Predict
        prediction = model.predict(final_input)[0]

        # Calculate Target Achievement %
        target_achievement = min((prediction / data['targeted_productivity']) * 100, 100)

        # Dynamic summary
        summary = (
            f"Predicted productivity: {round(prediction, 2)}. "
            "Focus on efficiency and task allocation for improvement."
        )

        return render_template(
            'result.html',
            prediction=round(prediction, 4),
            summary=summary,
            target_achievement=round(target_achievement, 1),
            targeted_productivity=data['targeted_productivity']
        )

    except Exception as e:
        return str(e)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

