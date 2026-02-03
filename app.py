import streamlit as st
import joblib
import numpy as np

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Sales Prediction",
    page_icon="📊",
    layout="centered"
)

# ---------------- LOAD MODEL ----------------
model = joblib.load("sales_model.pkl")

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.main {
    background-color: #f5f7fa;
}

.header {
    background: linear-gradient(90deg, #667eea, #764ba2);
    padding: 20px;
    border-radius: 12px;
    text-align: center;
    color: white;
    font-size: 30px;
    font-weight: bold;
}

.subtext {
    text-align: center;
    color: #555;
    margin-top: 10px;
}

.card {
    background-color: white;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
    margin-top: 25px;
}

.footer {
    text-align: center;
    font-size: 13px;
    color: #777;
    margin-top: 40px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown('<div class="header">📊 Sales Prediction App</div>', unsafe_allow_html=True)
st.markdown('<p class="subtext">Predict monthly sales using store information</p>', unsafe_allow_html=True)

# ---------------- INPUT CARD ----------------
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("🧾 Enter Store Details")

col1, col2 = st.columns(2)

with col1:
    advertising = st.number_input("📢 Advertising Spend (₹)", min_value=0, step=1000)

with col2:
    store_size = st.number_input("🏬 Store Size (sq ft)", min_value=0, step=50)

employees = st.number_input("👥 Number of Employees", min_value=0, step=1)

st.markdown('</div>', unsafe_allow_html=True)

# ---------------- PREDICTION ----------------
st.markdown('<div class="card">', unsafe_allow_html=True)

if st.button("🚀 Predict Sales", use_container_width=True):
    input_data = np.array([[advertising, store_size, employees]])
    prediction = model.predict(input_data)

    st.markdown(
        f"<h2 style='text-align:center;color:#27AE60;'>💰 Predicted Monthly Sales<br>₹ {int(prediction[0]):,}</h2>",
        unsafe_allow_html=True
    )

st.markdown('</div>', unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown(
    '<div class="footer">Built with ❤️ using Machine Learning & Streamlit</div>',
    unsafe_allow_html=True
)
