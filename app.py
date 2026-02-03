import streamlit as st
import joblib
import numpy as np

# Page configuration
st.set_page_config(
    page_title="Sales Prediction App",
    page_icon="📊",
    layout="centered"
)

# Load model
model = joblib.load("sales_model.pkl")

# Title
st.markdown(
    "<h1 style='text-align: center; color: #2C3E50;'>📊 Sales Prediction App</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align: center;'>Predict monthly sales using store details</p>",
    unsafe_allow_html=True
)

st.divider()

# Input section
st.subheader("🔢 Enter Store Details")

col1, col2 = st.columns(2)

with col1:
    advertising = st.number_input(
        "Advertising Spend (₹)",
        min_value=0,
        step=1000
    )

with col2:
    store_size = st.number_input(
        "Store Size (sq ft)",
        min_value=0,
        step=50
    )

employees = st.number_input(
    "Number of Employees",
    min_value=0,
    step=1
)

st.divider()

# Prediction button
if st.button("🚀 Predict Sales", use_container_width=True):
    input_data = np.array([[advertising, store_size, employees]])
    prediction = model.predict(input_data)

    st.success(f"💰 Predicted Monthly Sales: ₹ {int(prediction[0]):,}")
