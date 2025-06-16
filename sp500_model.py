import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load('model.pk1')

st.title("S&P 500 Close Price Predictor")

st.write("Enter the features below:")

# Example inputs (you'll replace with your actual features)
# Let's say you have 5 features for simplicity — adjust as needed
feature1 = st.number_input('sp500 open')
feature2 = st.number_input('nasdaq close')
feature3 = st.number_input('gold close')
feature4 = st.number_input('oil close')
feature5 = st.number_input('eur_usd')

if st.button('Predict'):
    # Create input array
    features = np.array([[feature1, feature2, feature3, feature4, feature5]])
    prediction = model.predict(features)
    st.success(f"Predicted S&P 500 close: {prediction[0]:.2f}")
    st.write('work')