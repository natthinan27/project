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

grouped_data = df.groupby(['Gender', 'size']).size().reset_index(name='count')
pivot_table = pd.pivot_table(grouped_data, values='count', index='Gender', columns='size', fill_value=0)
fig, ax = plt.subplots(figsize=(15, 7))
colors = ['#57b199', '#7fc15a', '#ffa53b']
pivot_table.plot.pie(subplots=True, autopct='%1.1f%%', ax=ax, colors=colors)
plt.axis('equal')
st.pyplot(fig)

#st.altair_chart(altair_chart, use_container_width=False, theme="streamlit")
group_age = df.groupby(['Item Purchased', 'Gender']).size().reset_index(name='count')
st.bar_chart(group_age, x='Item Purchased', y='count', color='Gender', height=400)



