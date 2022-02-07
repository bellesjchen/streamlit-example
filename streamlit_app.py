from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import requests
import json

st.markdown('Streamlit is **_really_ cool**.')
st.metric(label="Temperature", value="70 °F", delta="1.2 °F")

{'result': ["hello","World"]}

data = '{"model":"default"}'
response = requests.post('http://colormind.io/api/', data=data)
response.json()

