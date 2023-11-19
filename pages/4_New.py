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

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.bar_chart(chart_data)

#dftext=pd.DataFrame(df)
#st.bar_chart(dftext['Item Purchased','Color'].value_counts())

#grouped_data = df.groupby(['Season', 'Gender']).size().reset_index(name='count')
#pivot_table = pd.pivot_table(grouped_data, values='count', index='Season', columns='Gender', fill_value=0)
#plt.figure(figsize=(15, 7))
#pivot_table.plot(kind='line', marker='o', linewidth=2)
#plt.xlabel('Season')
#plt.ylabel('Count')
#plt.title('Line Chart of Gender Distribution by Season')
#plt.legend(title='Gender')
#plt.grid(True)
#plt.show()


#grouped_data = df.groupby(['Season', 'Gender']).size().reset_index(name='count')
#pivot_table = pd.pivot_table(grouped_data, values='count', index='Season', columns='Gender', fill_value=0)

# Plot the line chart
#plt.plot(pivot_table.index, pivot_table['Gender'])
#plt.xlabel('Season')
#plt.ylabel('Gender')
#plt.title('Line Chart of Gender Distribution by Season')
#plt.show


#st.line_chart(
 #  chart_data, x="stock_index_price", y=["interest_rate", "unemployment_rate"], color=["#FF0000", "#0000FF"]  # Optional)


