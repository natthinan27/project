import json
import time
import requests
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.header("Show Data Index Price")
df=pd.read_csv("./Data/shopping22.csv")
st.write(df.head(10))

st.header("Show chart")
chart_data=pd.read_csv("./Data/shopping22.csv")

#st.altair_chart(altair_chart, use_container_width=False, theme="streamlit")
group_age = df.groupby(['Item Purchased', 'Gender']).size().reset_index(name='count')
st.bar_chart(group_age, x='Item Purchased', y='count', color='Gender', height=400)



