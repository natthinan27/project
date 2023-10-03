import json
import time
import requests
import streamlit as st
import pandas as pd

st.header("Show Data Index Price")
df=pd.read_csv("./Data/stock_index_price.csv")
st.write(df.head(10))


