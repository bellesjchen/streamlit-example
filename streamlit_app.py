from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import requests
import json
import requests
from colormap import rgb2hex

data = '{"model":"default"}'
response = requests.post('http://colormind.io/api/', data=data)
color_list = response.json()
R = color_list['result'][0][0]
G = color_list['result'][0][1]
B = color_list['result'][0][1]

a='#1aa3ff'

st.markdown('Streamlit is **_really_ cool**.')
st.metric(label="Temperature", value="70 °F", delta="1.2 °F")

col1, col2 ,col3= st.columns(3)
with col1:
     color1 = st.color_picker('pick the starting color',a,key=1)
     st.write(f"you picked {color1}")
with col2:
     color2 = st.color_picker('pick the ending color', a,key=2)
     st.write(f"you picked {color2}")
with col3:
     color3 = st.color_picker('pick the text color', a,key=3)
     st.write(f"you picked {color3}")
text=st.text_input(" the text you want to input")

def example(color1, color2, color3, content):
     st.markdown(f'<p style="text-align:center;background-image: linear-gradient(to right,{color1}, {color2});color:{color3};font-size:24px;border-radius:2%;">{content}</p>', unsafe_allow_html=True)
example(color1,color2,color3,text)
