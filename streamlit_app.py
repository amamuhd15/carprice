# streamlit_app.py
import streamlit as st
import joblib
import pandas as pd
#import json

#with open("dropdown_options.json", "r") as f:
    #options = json.load(f)

st.set_page_config(page_title="Car Price Prediction App", layout="wide")

# --- Center the entire layout using CSS ---
st.markdown("""
    <style>
        .stButton button {
            width: 100%;
            border-radius: 10px;
            height: 50px;
            font-size: 20px;
            background-color: #4CAF50;
            color: white;
             margin-left: auto;
            margin-right: auto;
            text-align: center;
        }
    </style>
    </div>
""", unsafe_allow_html=True)

# Load Model
pipeline = joblib.load("car_price_model.pkl")

# --- UI Header ---
st.markdown("<h1 style='text-align: center;'>🚗 Car Price Prediction App</h1>", unsafe_allow_html=True)
st.write("")


st.markdown("<h3 style='text-align:center;'>Enter Car Details</h3>", unsafe_allow_html=True)
st.write("")

# Load your dataset so we can extract dropdown options
cpd = pd.read_csv("carprice_dataset.csv")

# Create dropdown option lists
OPTIONS_COMPANY = sorted(cpd["Company Name"].unique())
OPTIONS_MODEL = sorted(cpd["Model Name"].unique())
OPTIONS_LOCATION = sorted(cpd["Location"].unique())
OPTIONS_ENGINE_TYPE = sorted(cpd["Engine Type"].unique())
OPTIONS_COLOR = sorted(cpd["Color"].unique())
OPTIONS_ASSEMBLY = sorted(cpd["Assembly"].unique())
OPTIONS_BODY_TYPE = sorted(cpd["Body Type"].unique())
OPTIONS_TRANSMISSION = sorted(cpd["Transmission Type"].unique())
OPTIONS_REGSTATUS = sorted(cpd["Registration Status"].unique())

# Load model
model = joblib.load("car_price_model.pkl")

#st.title("🚗 Car Price Prediction System")

#st.write("Fill in the details below to estimate car price:")

# Row 1
col1, col2 = st.columns(2)
with col1:
    company = st.selectbox("Company Name", OPTIONS_COMPANY)
    engine_type = st.selectbox("Engine Type", OPTIONS_ENGINE_TYPE)
    transmission_type = st.selectbox("Transmission Type", OPTIONS_TRANSMISSION)
    mileage = st.number_input("Mileage (km)", min_value=0, max_value=300000, value=50000)
    assembly = st.selectbox("Assembly", OPTIONS_ASSEMBLY)
    car_age = st.number_input("Car Age (years)", min_value=0, max_value=30, value=5)

with col2:
    model_name = st.selectbox("Model Name", OPTIONS_MODEL)
    body_type = st.selectbox("Body Type", OPTIONS_BODY_TYPE)
    location = st.selectbox("Location", OPTIONS_LOCATION)
    engine_capacity = st.number_input("Engine Capacity (cc)", min_value=600, max_value=5000, value=1300)
    registration_status = st.selectbox("Registration Status", OPTIONS_REGSTATUS)
    color = st.selectbox("Color", OPTIONS_COLOR)


#prepare inut
if st.button("Predict Price"):
    user_input = {
        "Company Name": company,
        "Model Name": model_name,
        "Car_Age": car_age,
        "Location": location,
        "Mileage": mileage,
        "Engine Type": engine_type,
        "Engine Capacity": engine_capacity,
        "Color": color,
        "Assembly": assembly,
        "Body Type": body_type,
        "Transmission Type": transmission_type,
        "Registration Status": registration_status
    }

    df = pd.DataFrame([user_input])
    prediction = model.predict(df)[0]

    st.success(f"Estimated Car Price: **₦{int(prediction):,}**")
