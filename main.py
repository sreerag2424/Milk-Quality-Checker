import base64
import pickle
import streamlit as st
import os
import numpy as np  
def set_background(image_file):
    with open(image_file, "rb") as img_file:
        base64_image = base64.b64encode(img_file.read()).decode()
    
    background_style = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpeg;base64,{base64_image}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(background_style, unsafe_allow_html=True)

# Call the function with your background image
set_background("static/bg.jpg")

# Streamlit App Title
st.markdown("<h1 style='text-align: center; color: white;'>🥛 Milk Quality Checker</h1>", unsafe_allow_html=True)

# Load Model
file_path = os.path.join("model", "knn_model.pkl")

# Check if file exists before loading
if not os.path.exists(file_path):
    st.error("Model file not found! Please ensure 'knn_model.pkl' is in the 'knn_model' directory.")
else:
    with open(file_path, 'rb') as f:
        model = pickle.load(f)

# Input Fields
ph = st.number_input("Insert a pH Value ", min_value=3.0, max_value=9.5)
tm = st.slider("Insert Temperature of Milk ", min_value=34, max_value=90)
ta = st.number_input("Insert Taste of Milk ", min_value=0, max_value=1)
om = st.number_input("Insert Odor of Milk ", min_value=0, max_value=1)
fm = st.number_input("Insert Fat of Milk ", min_value=0, max_value=1)
tu = st.number_input("Insert Turbidity of Milk ", min_value=0, max_value=1) 
cm = st.number_input("Insert Colour Value of Milk ", min_value=240, max_value=255)


# Prediction
if st.button("Predict"):
    if 'model' in locals():  # Check if model is loaded
        input_data = np.array([[ph, tm, ta, om, fm, tu, cm]])
        prediction = model.predict(input_data)
        st.write("Quality of Milk is:", prediction[0])
    else:
        st.error("Model not loaded. Check the file path.")