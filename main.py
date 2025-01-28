import pickle
import streamlit as st
import os
import numpy as np  

# Streamlit App Title
st.title("Milk Quality Checker")

# Load Model
file_path = os.path.join("knn_model.pkl")

# Check if file exists before loading
if not os.path.exists(file_path):
    st.error("Model file not found! Please ensure 'knn_model.pkl' is in the 'knn_model' directory.")
else:
    with open(file_path, 'rb') as f:
        model = pickle.load(f)

# Input Fields
ph = st.number_input("Insert a pH Value (3-9.5)", min_value=3.0, max_value=9.5)
tm = st.number_input("Insert Temperature of Milk (34-90)", min_value=34, max_value=90)
ta = st.number_input("Insert Taste of Milk (0/1)", min_value=0, max_value=1)
om = st.number_input("Insert Odor of Milk (0/1)", min_value=0, max_value=1)
fm = st.number_input("Insert Fat of Milk (0/1)", min_value=0, max_value=1)
tu = st.number_input("Insert Turbidity of Milk (0/1)", min_value=0, max_value=1)
cm = st.number_input("Insert Colour of Milk (240-255)", min_value=240, max_value=255)

# Prediction
if st.button("Predict"):
    if 'model' in locals():  # Check if model is loaded
        input_data = np.array([[ph, tm, ta, om, fm, tu, cm]])
        prediction = model.predict(input_data)
        st.write("Quality of Milk is:", prediction[0])
    else:
        st.error("Model not loaded. Check the file path.")
