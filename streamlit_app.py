from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

st.markdown('Streamlit is **_really_ cool**.')
st.metric(label="Temperature", value="70 °F", delta="1.2 °F")

url = 'http://colormind.io/api/'
r = requests.get(url)
print("Status code:", r.status_code)
