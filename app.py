import streamlit as st
from streamlit_lottie import st_lottie
import  json
import requests

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)
lottie_tractor3 = load_lottiefile(r"lottie/tractor-3.json")

st.markdown("""
    <style>
            
    div.stButton > button:first-child {
        border: 3px solid #8284edff;
        border-radius: 0px;
        padding: 10px 20px;    
        height: 50px;
        width: 150px;
        margin-top: 20px;
    }            

    </style>
""", unsafe_allow_html=True)


st.title("AnyField's Crop Recommendation System")
st.text("Plant the right crop for YOUR field's conditions!")


col1, col2, col3 = st.columns([1, 1, 1])
with col3:
    if st.button("Let's go \u00A0 \u2192"):
        st.switch_page("pages/form.py")

col1, col2, col3 = st.columns([1, 3, 1])
with col2:
    st_lottie(lottie_tractor3, speed=1, width=380, height=260, key="tractor")
