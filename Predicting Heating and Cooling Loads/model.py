import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import pickle

# Load the dataset
df = pd.read_csv(r"C:\Users\anavi\Documents\CO22307_energy_efficiency_dataset.csv")

# Features (independent variables)
X = df.drop(['Heating_Load', 'Cooling_Load'], axis=1)

# Targets (dependent variables — BOTH loads)
y = df[['Heating_Load', 'Cooling_Load']]  # Important: 2-column target

# Model
model = RandomForestRegressor()
model.fit(X, y)

# Save the model
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)



