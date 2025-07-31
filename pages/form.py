import streamlit as st
import joblib
import numpy as np
from streamlit_lottie import st_lottie
import  json
import requests


def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

lottie_tractor3 = load_lottiefile(r"lottie/tractor-3.json")

try:
    # If using joblib compression
    best_gbc = joblib.load('best_gbc_model.pkl')
    
    # Or if using gzip
    # with gzip.open('best_gbc_model.pkl.gz', 'rb') as f:
    #     best_gbc = pickle.load(f)
    
    model_loaded = True
except Exception as e:
    st.error(f"Error loading model: {str(e)}")
    model_loaded = False


st.markdown("""
    <style>
            
    div.stButton > button:first-child {
        border: 3px solid #8284edff;
        border-radius: 9px;
        padding: 10px 20px;    
        height: 50px;
        width: 250px;
    }            

    </style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 3, 1])
with col2:
    st_lottie(lottie_tractor3, speed=1, width=380, height=260, key="tractor")


st.subheader("Please fill in your site's environmental conditions:")

st.markdown("<br>", unsafe_allow_html=True)

st.write("#### Soil Type: ")
soil_type = st.selectbox("Type", ["Acidic Soil", "Alkaline Soil", "Loamy Soil", "Neutral Soil", "Peaty Soil"])

st.markdown("<br>", unsafe_allow_html=True)

st.write("#### Temperature: ")

#temp range
min_temp = 0.0
max_temp = 60.0
default_temp = 25.0

if "temp" not in st.session_state:
    st.session_state.temp=default_temp

def update_slider():
    st.session_state.temp = st.session_state.temp_input

def update_input():
    st.session_state.temp = st.session_state.temp_slider

col1, col2 = st.columns(2)
with col1:
    st.slider("Degree Celcius (°C):",
               min_value=min_temp, 
               max_value=max_temp,
               key="temp_slider", 
               step=0.05,
               value=st.session_state.temp, 
               on_change=update_input)

with col2:
    st.number_input("Degree Celcius (°C):",
                    min_value=min_temp,
                    max_value=max_temp,
                    key="temp_input",
                    step=0.05,
                    value=st.session_state.temp,
                    on_change=update_slider)

st.write(f"Selected Temperature: {st.session_state.temp:.2f} °C")
temp = st.session_state.temp

st.markdown("<br>", unsafe_allow_html=True)

st.write("#### Humidity: ")

#humidity range
min_hum = 0.0
max_hum = 100.0
default_hum = 50.0

if "hum" not in st.session_state:
    st.session_state.hum=default_hum

def update_slider():
    st.session_state.hum = st.session_state.hum_input

def update_input():
    st.session_state.hum = st.session_state.hum_slider

col1, col2 = st.columns(2)
with col1:
    st.slider("Percent (%):",
               min_value=min_hum, 
               max_value=max_hum,
               key="hum_slider", 
               step=0.05,
               value=st.session_state.hum, 
               on_change=update_input)

with col2:
    st.number_input("Percent (%):",
               min_value=min_hum, 
               max_value=max_hum,
               key="hum_input", 
               step=0.05,
               value=st.session_state.hum, 
               on_change=update_slider)

st.write(f"Selected Humidity: {st.session_state.hum:.2f} %")
hum = st.session_state.hum

st.markdown("<br>", unsafe_allow_html=True)

st.write("#### Rainfall: ")

#rainfall range
min_rain = 0.0
max_rain = 400.0
default_rain = 100.0

if "rain" not in st.session_state:
    st.session_state.rain=default_rain

def update_slider():
    st.session_state.rain = st.session_state.rain_input

def update_input():
    st.session_state.rain = st.session_state.rain_slider


col1, col2 = st.columns(2)
with col1:
    st.slider("Milimeters (mm):",
            min_value=min_rain, 
            max_value=max_rain,
            key="rain_slider", 
            step=0.05,
            value=st.session_state.rain, 
            on_change=update_input)

with col2:
    st.number_input("Milimeters (mm):",
            min_value=min_rain, 
            max_value=max_rain,
            key="rain_input",
            step=0.05,
            value=st.session_state.rain, 
            on_change=update_slider)

st.write(f"Selected Rainfall: {st.session_state.rain:.2f} mm")
rain = st.session_state.rain
st.markdown("</div>", unsafe_allow_html=True)


st.write("#### Soil pH: ")

#ph range
min_ph = 0.0
max_ph = 14.0
default_ph = 7.0

if "ph" not in st.session_state:
    st.session_state.ph=default_ph

def update_slider():
    st.session_state.ph = st.session_state.ph_input

def update_input():
    st.session_state.ph = st.session_state.ph_slider


col1, col2 = st.columns(2)
with col1:
    st.slider("Power Of Hydrogen (pH):",
               min_value=min_ph, 
               max_value=max_ph,
               key="ph_slider",
               step=0.05,
               value=st.session_state.ph, 
               on_change=update_input)

with col2:
    st.number_input("Power Of Hydrogen (pH):",
               min_value=min_ph, 
               max_value=max_ph,
               key="ph_input",
               step=0.05,
               value=st.session_state.ph, 
               on_change=update_slider)

st.write(f"Selected pH: {st.session_state.ph:.2f}")
ph = st.session_state.ph

st.markdown("<br>", unsafe_allow_html=True)

st.write("#### Nitrogen content in soil: ")

#nitrogen range
min_nitrogen = 50.0
max_nitrogen = 100.0
default_nitrogen = 55.0

if "nitrogen" not in st.session_state:
    st.session_state.nitrogen=default_nitrogen

def update_slider():
    st.session_state.nitrogen = st.session_state.nitrogen_input

def update_input():
    st.session_state.nitrogen = st.session_state.nitrogen_slider


col1, col2 = st.columns(2)
with col1:
    st.slider("Parts Per Million (ppm):",
               min_value=min_nitrogen, 
               max_value=max_nitrogen,
               key="nitrogen_slider",
               step=0.05,
               value=st.session_state.nitrogen, 
               on_change=update_input)

with col2:
    st.number_input("Parts Per Million (ppm):",
               min_value=min_nitrogen, 
               max_value=max_nitrogen,
               key="nitrogen_input",
               step=0.05,
               value=st.session_state.nitrogen, 
               on_change=update_slider)
    

st.write(f"Selected Nitrogen content: {st.session_state.nitrogen:.2f} ppm")
nitrogen = st.session_state.nitrogen

st.markdown("<br>", unsafe_allow_html=True)

st.write("#### Phosphorus content in soil: ")

#phosphorus range
min_phosphorus = 30.0
max_phosphorus = 150.0
default_phosphorus = 50.0

if "phosphorus" not in st.session_state:
    st.session_state.phosphorus=default_phosphorus

def update_slider():
    st.session_state.phosphorus = st.session_state.phosphorus_input

def update_input():
    st.session_state.phosphorus = st.session_state.phosphorus_slider


col1, col2 = st.columns(2)
with col1:
    st.slider("Parts Per Million (ppm):",
               min_value=min_phosphorus, 
               max_value=max_phosphorus,
               key="phosphorus_slider",
               step=0.05,
               value=st.session_state.phosphorus, 
               on_change=update_input)

with col2:
    st.number_input("Parts Per Million (ppm):",
               min_value=min_phosphorus, 
               max_value=max_phosphorus,
               key="phosphorus_input",
               step=0.05,
               value=st.session_state.phosphorus, 
               on_change=update_slider)
    

st.write(f"Selected Phosphorus content: {st.session_state.phosphorus:.2f} ppm")
phosphorus = st.session_state.phosphorus

st.markdown("<br>", unsafe_allow_html=True)

st.write("#### Potassium content in soil: ")

#potassium range
min_potassium = 40.0
max_potassium = 150.0
default_potassium = 60.0

if "potassium" not in st.session_state:
    st.session_state.potassium=default_potassium

def update_slider():
    st.session_state.potassium = st.session_state.potassium_input

def update_input():
    st.session_state.potassium = st.session_state.potassium_slider


col1, col2 = st.columns(2)
with col1:
    st.slider("Parts Per Million (ppm):",
               min_value=min_potassium, 
               max_value=max_potassium,
               key="potassium_slider",
               step=0.05,
               value=st.session_state.potassium, 
               on_change=update_input)

with col2:
    st.number_input("Parts Per Million (ppm):",
               min_value=min_potassium, 
               max_value=max_potassium,
               key="potassium_input",
               step=0.05,
               value=st.session_state.potassium, 
               on_change=update_slider)

st.write(f"Selected Potassium content: {st.session_state.potassium:.2f} ppm")
potassium = st.session_state.potassium

st.markdown("<br>", unsafe_allow_html=True)
st.write("#### Organic Carbon content in soil: ")

#carbon range
min_carbon = 0.5
max_carbon = 3.0
default_carbon = 1.0

if "carbon" not in st.session_state:
    st.session_state.carbon=default_carbon

def update_slider():
    st.session_state.carbon = st.session_state.carbon_input

def update_input():
    st.session_state.carbon = st.session_state.carbon_slider


col1, col2 = st.columns(2)
with col1:
    st.slider("Percent (%):",
            min_value=min_carbon, 
            max_value=max_carbon,
            key="carbon_slider",
            step=0.05,
            value=st.session_state.carbon, 
            on_change=update_input)

with col2:
    st.number_input("Percent (%):",
            min_value=min_carbon, 
            max_value=max_carbon,
            key="carbon_input",
            step=0.05,
            value=st.session_state.carbon, 
            on_change=update_slider)
    

st.write(f"Selected Carbon content: {st.session_state.carbon:.2f} %")
carbon = st.session_state.carbon



# OHE for soil type
soil_types_order = ["Acidic Soil", "Alkaline Soil", "Loamy Soil", "Neutral Soil", "Peaty Soil"]
soil_type_ohe = [1 if soil_type == s else 0 for s in soil_types_order]

# Combine numerical features and OHE features into a single input array
input_features = np.array([[temp, hum, rain, ph,
                            nitrogen, phosphorus, potassium, carbon] + soil_type_ohe])

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)


col1, col2, col3 = st.columns([1, 1, 1]) 
with col2:
    submit =  st.button("Get Crop Recommendation!")



if submit:
    # Make prediction
    prediction = best_gbc.predict(input_features)
    predicted_crop = prediction[0]
    # Display result
    with st.container():
        st.markdown("<br>", unsafe_allow_html=True)
        st.success(f"Recommended Crop: {predicted_crop}")