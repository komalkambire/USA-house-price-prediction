import streamlit as st
import pickle
import numpy as np

# Load the trained model
model = pickle.load(open('model.pkl', 'rb'))

st.title("🏠 USA House Price Prediction")

bedrooms = st.slider("Number of Bedrooms", 1, 10)
bathrooms = st.slider("Number of Bathrooms", 1, 10)
sqft = st.number_input("Square Foot Area")
location = st.selectbox("Location", ['California', 'Texas', 'New York','India'])

# Dummy encoding
location_dict = {'California': 0, 'Texas': 1, 'New York': 2,'India':3}
loc = location_dict[location]

if st.button("Predict"):
    input_data = np.array([[bedrooms, bathrooms, sqft, loc]])
    prediction = model.predict(input_data)
    st.success(f"Predicted Price: ${prediction[0]:,.2f}")

