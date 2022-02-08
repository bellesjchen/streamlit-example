from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import requests
import json
import requests


data = '{"model":"default"}'
response = requests.post('http://colormind.io/api/', data=data)
color_list = response.json()
R1 = color_list['result'][0][0]
G1 = color_list['result'][0][1]
B1 = color_list['result'][0][2]


st.markdown('I am trying **_cool_ api**.')
st.metric(label="Temperature", value="70 °F", delta="1.2 °F")
if st.button('change the word color'):
 st.markdown('<p style="font-family:sans-serif; color:rgb(%d,%d,%d); font-size: 42px;">color changed</p >' %(R1,G1,B1),unsafe_allow_html=True)
