import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Load trained model pipeline
with open('rf_pipeline_new_model.pkl', 'rb') as f:
    model = pickle.load(f)

# --- UI ---
st.title("🚦 Traffic Congestion Predictor")
st.markdown("Provide inputs below to predict the **Congestion Level**")

# Area names based on OHE seen during training
area_names = [
    'Indiranagar', 'Whitefield', 'Koramangala', 'Hebbal',
    'Jayanagar', 'M.G. Road', 'Electronic City', 'Yeshwanthpur'
]

# 1. Area Name (Dropdown)
area = st.selectbox("Area Name", options=[None] + area_names)

# 2. Other Inputs — Sliders/number_inputs
avg_speed = st.slider("Average Speed (km/h)", 0.0, 100.0, 50.0, step=0.1)
ped_count = st.slider("Pedestrian and Cyclist Count", 0, 500, 100)
tti = st.slider("Travel Time Index", 0.0, 3.0, 1.0, step=0.01)
traffic_vol = st.slider("Traffic Volume", 0, 100000, 30000)

# Optional advanced sliders
env_impact = st.slider("Environmental Impact", 0.0, 300.0, 100.0, step=0.1)
incident_reports = st.slider("Incident Reports", 0, 10, 1)
road_cap_util = st.slider("Road Capacity Utilization (%)", 0.0, 100.0, 50.0, step=0.1)

# Button
if st.button("🚀 Predict Congestion Level"):

    # Create dictionary of inputs with None values treated as np.nan
    input_data = {
        'Area Name': area if area else np.nan,
        'Average Speed': avg_speed,
        'Pedestrian and Cyclist Count': ped_count,
        'Travel Time Index': tti,
        'Traffic Volume': traffic_vol,
        'Environmental Impact': env_impact,
        'Incident Reports': incident_reports,
        'Road Capacity Utilization': road_cap_util
    }

    # Convert to single-row DataFrame
    input_df = pd.DataFrame([input_data])

    # Predict
    prediction = model.predict(input_df)[0]

    # Map encoded label to category
    label_map = {0: "Low", 1: "Medium", 2: "High"}
    result = label_map.get(prediction, "Unknown")

    # Display result
    st.success(f"📊 Predicted Congestion Level: **{result}**")
