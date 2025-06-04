import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("age_model.pkl")

st.title("🧠 Human Age Prediction App")
st.write("Enter your biological and lifestyle details to predict your estimated age.")

# Collect inputs
height = st.number_input("Height (cm)", 100, 250)
weight = st.number_input("Weight (kg)", 30, 200)
cholesterol = st.number_input("Cholesterol Level (mg/dL)", 100, 300)
bmi = st.number_input("BMI", 10.0, 40.0)
glucose = st.number_input("Blood Glucose Level (mg/dL)", 50, 250)
bone_density = st.number_input("Bone Density (g/cm²)", 0.5, 2.0)
vision = st.number_input("Vision Sharpness (0–1)", 0.0, 1.0)
hearing = st.number_input("Hearing Ability (dB)", 0.0, 100.0)
cognitive = st.slider("Cognitive Function (1–10)", 1, 10)
stress = st.slider("Stress Level (1–10)", 1, 10)
pollution = st.slider("Pollution Exposure (1–10)", 1, 10)
sun_exposure = st.slider("Sun Exposure (hours/day)", 0, 12)

if st.button("Predict Age"):
    features = np.array([[
        height, weight, cholesterol, bmi, glucose, bone_density,
        vision, hearing, cognitive, stress, pollution, sun_exposure
    ]])

    age = model.predict(features)[0]
    st.success(f"🧓 Predicted Biological Age: {age:.2f} years")
