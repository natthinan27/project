import streamlit as st
import plotly.express as px
import pandas as pd
import os
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title="Shoppinge!!!", page_icon=":bar_chart:",layout="wide")

st.title(" :bar_chart: Shopping")
st.markdown('<style>div.block-container{padding-top:1rem;}</style>',unsafe_allow_html=True)

uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)