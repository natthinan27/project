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


#dftext=pd.DataFrame(df)
#st.bar_chart(dftext['Item Purchased','Color'].value_counts())

#grouped_data = df.groupby(['Season', 'Gender']).size().reset_index(name='count')
#pivot_table = pd.pivot_table(grouped_data, values='count', index='Season', columns='Gender', fill_value=0)
#fig, ax = plt.subplots(figsize=(15, 7))
#colors = ['#57b199', '#7fc15a', '#ffa53b','#BB8FCE']
#pivot_table.plot.pie(subplots=True, autopct='%1.1f%%', ax=ax, colors=colors)
#plt.axis('equal')
#st.pyplot(fig)

fig, ax = plt.subplots(figsize=(15, 7))
colors = ['#F7DC6F', '#7fc15a', '#ffa53b','#BB8FCE']
pivot_table.plot.bar(stacked=True, color=colors, ax=ax)

plt.legend(title='Gender', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xlabel('Season')
plt.ylabel('Count')
plt.title('Gender Distribution by Season')

st.pyplot(fig)

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


