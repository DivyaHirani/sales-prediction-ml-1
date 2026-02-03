import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("sales_model.pkl")

st.title("📊 Sales Prediction App")

st.write("Enter store details to predict monthly sales")

advertising = st.number_input("Advertising Spend", min_value=0)
store_size = st.number_input("Store Size (sq ft)", min_value=0)
employees = st.number_input("Number of Employees", min_value=0)

if st.button("Predict Sales"):
    input_data = np.array([[advertising, store_size, employees]])
    prediction = model.predict(input_data)
    st.success(f"Predicted Monthly Sales: ₹ {int(prediction[0])}")
