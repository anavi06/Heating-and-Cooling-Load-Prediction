from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# Define feature columns
features = ['Relative_Compactness', 'Surface_Area', 'Wall_Area', 'Roof_Area',
            'Overall_Height', 'Orientation', 'Glazing_Area', 'Glazing_Area_Distribution']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    user_input = {}
    for col in features:
        user_input[col] = float(request.form[col])

    input_df = pd.DataFrame([user_input], columns=features)

    # Get prediction
    prediction = model.predict(input_df)  # Should return array shape (1, 2)
    heating_load = round(prediction[0][0], 2)
    cooling_load = round(prediction[0][1], 2)

    return render_template('result.html',
                           heating=heating_load,
                           cooling=cooling_load)

if __name__ == '__main__':
    app.run(debug=True)
