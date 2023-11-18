import json
import time
import requests
import streamlit as st
import pandas as pd

st.header("Show Data Index Price")
df=pd.read_csv("./Data/shopping22.csv")
st.write(df.head(10))

st.header("Show chart")
chart_data=pd.read_csv("./Data/shopping22.csv")

import matplotlib.pyplot as plt

def plot(df):
    # Select a column to plot
    column_name = 'Age'

    # Create a line plot of the selected column
    plt.plot(df['index'], df[column_name])

    # Add labels and title to the plot
    plt.xlabel('index')
    plt.ylabel(column_name)
    plt.title('Plot of ' + column_name)

    # Display the plot
    plt.show()
#st.line_chart(
 #  chart_data, x="stock_index_price", y=["interest_rate", "unemployment_rate"], color=["#FF0000", "#0000FF"]  # Optional)


