import json
import time
import requests
import streamlit as st

st.set_page_config(
    page_title="การวิเคราะห์พฤติกรรมผู้บริโภคโดยการจัดกลุ่มแบบเคมีน",
    page_icon= ":bar_chart:",
)
st.sidebar.success("เลือกรายการด้านบน.")

html_1 = """
<div style="background-color:#dab3ff;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>การวิเคราะห์พฤติกรรมผู้บริโภคโดยการจัดกลุ่มแบบเคมีน111</h5></center>
<center><h5>Analyzes Consumer Behavior by K-means clustering</h5></center>
</div>
</div>
"""
st.markdown(html_1, unsafe_allow_html=True)
st.markdown("")

