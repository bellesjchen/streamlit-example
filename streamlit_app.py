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
response.json()

st.markdown('Streamlit is **_really_ cool**.')
st.metric(label="Temperature", value="70 °F", delta="1.2 °F")

col1, col2 ,col3= st.beta_columns(3)
with col1:
     color1 = st.color_picker('pick the starting color', '#1aa3ff',key=1)
     st.write(f"you picked {color1}")
with col2:
     color2 = st.color_picker('pick the ending color', '#00ff00',key=2)
     st.write(f"you picked {color2}")
with col3:
     color3 = st.color_picker('pick the text color', '#ffffff',key=3)
     st.write(f"you picked {color3}")
text=st.text_input(" what you need to add")

def example(color1, color2, color3, content):
     st.markdown(f'<p style="text-align:center;background-image: linear-gradient(to right,{color1}, {color2});color:{color3};font-size:24px;border-radius:2%;">{content}</p>', unsafe_allow_html=True)
example(color1,color2,color3,text)
