import streamlit as st
import numpy as np
import pickle

# Load the saved model
model = pickle.load(open('project2.pkl', 'rb'))

st.title("Diabetes Prediction App")
st.write("Enter the patient’s medical information below:")

# Input fields for medical data
pregnancies = st.number_input('Pregnancies', min_value=0)
glucose = st.number_input('Glucose Level', min_value=0)
bp = st.number_input('Blood Pressure', min_value=0)
skin_thickness = st.number_input('Skin Thickness', min_value=0)
insulin = st.number_input('Insulin Level', min_value=0)
bmi = st.number_input('BMI', min_value=0.0, format="%.1f")
dpf = st.number_input('Diabetes Pedigree Function', min_value=0.0, format="%.3f")
age = st.number_input('Age', min_value=0)

if st.button('Predict'):
    input_data = np.array([[pregnancies, glucose, bp, skin_thickness, insulin, bmi, dpf, age]])
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠️ The patient is likely to have diabetes.")
    else:
        st.success("✅ The patient is not likely to have diabetes.")
