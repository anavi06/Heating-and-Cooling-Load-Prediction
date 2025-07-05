## Heating-and-Cooling-Load-Prediction
# Introduction  
This is a beginner friendly web app using Flask, pandas and scikit-learn (sklearn) that predicts how much energy a building will need for heating and cooling.  
The prediction is based on basic building features like wall area, roof area, glazing, height, and more. It uses the Energy Efficiency dataset and a Random Forest Regressor model to make accurate predictions. The goal is to help in designing energy-efficient buildings by estimating how much energy is needed to heat or cool them.

# Files in this Project  
- `model.py`: Trains the Random Forest model and saves it as `model.pkl`  
- `App.py`: The main Flask app  
- `model.pkl`: The trained model (auto-generated after running `model.py`)  
- `templates/index.html`: Form for user input  
- `templates/result.html`: Web page to display Heating and Cooling Load prediction

