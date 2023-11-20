import json
import time
import requests
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.header("Show Data Index Price")
df=pd.read_csv("./Data/shopping22.csv")
st.write(df.head(10))

st.header("Show chart Gender and Size")
chart_data=pd.read_csv("./Data/shopping22.csv")
grouped_data = df.groupby(['Gender', 'Size']).size().reset_index(name='count')
pivot_table = pd.pivot_table(grouped_data, values='count', index='Gender', columns='Size', fill_value=0)
fig, ax = plt.subplots(figsize=(15, 7))
colors = ['#ff6699', '#6699ff']
pivot_table.plot.pie(subplots=True, autopct='%1.1f%%', ax=ax, colors=colors)
plt.axis('equal')
st.pyplot(fig)

#st.altair_chart(altair_chart, use_container_width=False, theme="streamlit")
st.header("Show chart Gender and Item Purchased")
chart_data=pd.read_csv("./Data/shopping22.csv")
group_age = df.groupby(['Item Purchased', 'Gender']).size().reset_index(name='count')
st.bar_chart(group_age, x='Item Purchased', y='count', color='Gender', height=400)

st.header("Show chart Category and Gender")
chart_data=pd.read_csv("./Data/shopping22.csv")
grouped_data = df.groupby(['Category', 'Gender']).size().reset_index(name='count')
pivot_table = pd.pivot_table(grouped_data, values='count', index='Category', columns='Gender', fill_value=0)
fig, ax = plt.subplots(figsize=(15, 7))
colors = ['#66ff99', '#ccccff','#ffff66','#66ffcc']
pivot_table.plot.pie(subplots=True, autopct='%1.1f%%', ax=ax, colors=colors)
plt.axis('equal')
st.pyplot(fig)

st.header("Show chart Gender and Age")
chart_data=pd.read_csv("./Data/shopping22.csv")
group_age = df.groupby(['Age', 'Gender']).size().reset_index(name='count')
st.bar_chart(group_age, x='Age', y='count', color='Gender', height=400)

