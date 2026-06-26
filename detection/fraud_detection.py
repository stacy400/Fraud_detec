import streamlit as st
import pandas as pd
import joblib
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model = joblib.load(os.path.join(BASE_DIR, "fraud_detection_model.pkl"))

st.title("Fraud Detection App")

st.markdown("This app predicts whether a transaction is fraudulent or not based on the input features.")

st.divider()

transaction_type = st.selectbox("Transaction Type", ["PAYMENT", "TRANSFER", "CASH_OUT", "DEPOSIT"])
amount = st.number_input("Transaction Amount", min_value=0.0,value=1000.0)
oldbalanceOrg = st.number_input("Old Balance Origin(sender)", min_value=0.0,value=1000.0)
newbalanceOrig = st.number_input("New Balance Origin(sender)", min_value=0.0,value=9000.0)
oldbalanceDest = st.number_input("Old Balance Destination(receiver)", min_value=0.0,value=0.0)
newbalanceDest = st.number_input("New Balance Destination(receiver)", min_value=0.0,value=0.0)

if st.button("Predict"):
    input_data = pd.DataFrame([{
        "type": transaction_type,
        "amount": amount,
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrig": newbalanceOrig,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest": newbalanceDest
    }])

    prediction = model.predict(input_data)[0]

    st.subheader(f"Prediction: {int(prediction)}")

    if prediction == 1:
        st.error("The transaction is predicted to be fraudulent.")
    else:
        st.success("The transaction is predicted to be legitimate.")