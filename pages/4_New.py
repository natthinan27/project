import json
import time
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner

st.header("Show Data Index Price")
df=pd.read_csv("./C:\AppServ\MySQL\project1\project\stock_index_price-2.csv")
st.write(df.head(10))


