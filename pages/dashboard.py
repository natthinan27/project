import streamlit as st
import plotly.express as px
import pandas as pd
import os
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title="Shoppinge!!!", page_icon=":bar_chart:",layout="wide")

st.title(" :bar_chart: Shopping")
st.markdown('<style>div.block-container{padding-top:1rem;}</style>',unsafe_allow_html=True)

fl = st.file_uploader(":file_folder: Upload a file",type=(["csv","txt","xlsx","xls"]))
if fl is not None:
    filename = fl.name
    st.write(filename)
    df = pd.read_csv(filename, encoding = "ISO-8859-1")
else:
    os.chdir("C:\\Users\\acer\\Desktop\\shopping")
    df = pd.read_csv("shopping22.csv", encoding = "ISO-8859-1")
    
    col1.col2 = st.colums((2))
    df["Order Data"] = pd.to_datetime(df["Order Data"])

    # Getting the min and max data
    startData = pd.to_datatime(df["Order Data"])
    endData = pd.to_datatime(df["Order Data"])

    with col1:
        date1 = pd.to_datatime(st.date_input("start Data",startData))

    with col2:
        date2 = pd.to_datatime(st.date_input("End Data",endData))

    df = df[(df["Order Data"] >= date1) & (df["Order Data"] <= date2)].copy()

    st.sidebar.header("Choose your filter:")
    region = st.sidebar.multiselect("Pick  your Region",df["Region"].unique())

