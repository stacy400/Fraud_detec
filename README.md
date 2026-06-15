# Fraud Detection Project

A small fraud detection application built with Streamlit. The app loads a pre-trained model and predicts whether a transaction is fraudulent based on user-provided transaction details.

## Project Structure

- `detection/fraud_detection.py` - Streamlit app for user interaction and prediction.
- `detection/fraud_detection_model.pkl` - Pre-trained fraud detection model.
- `detection/AIML Dataset.csv` - Transaction dataset used for analysis and model training.
- `detection/Analysis.ipynb` - Jupyter notebook for exploratory data analysis and model development.

## Requirements

- Python 3.8+
- `streamlit`
- `pandas`
- `joblib`

## Setup

1. Open a terminal and navigate to the project folder:

```powershell
cd c:\Users\Admin\OneDrive\Desktop\fraud_detec\detection
```

2. Install dependencies:

```powershell
pip install streamlit pandas joblib
```

## Running the App

From the `detection` directory, run:

```powershell
streamlit run fraud_detection.py
```

This will start a local Streamlit server and open the fraud detection interface in your browser.

## Usage

- Select a transaction type.
- Enter transaction amount and account balance values.
- Click `Predict` to see whether the transaction is classified as fraudulent or legitimate.

## Notes

- The model is loaded from `detection/fraud_detection_model.pkl`.
- If you retrain the model, replace the `.pkl` file with the new version.
- Use `Analysis.ipynb` to inspect the dataset and review model training steps.
