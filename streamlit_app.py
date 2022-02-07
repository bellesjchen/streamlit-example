from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import requests as req
import json

st.markdown('Streamlit is **_really_ cool**.')
st.metric(label="Temperature", value="70 °F", delta="1.2 °F")


data = '{"model":"default"}'
response = requests.post('http://colormind.io/api/', data=data)
response.json()

{'result': [[71, 94, 97], [109, 152, 137], [183, 213, 193], [243, 239, 204], [240, 153, 122]]}
