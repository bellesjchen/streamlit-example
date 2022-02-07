from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import requests
import json

st.markdown('Streamlit is **_really_ cool**.')
st.metric(label="Temperature", value="70 °F", delta="1.2 °F")

def query():
    url = 'http://colormind.io/api/'
    response = req.get(url, data={"model":"default"}
    )
    print(response.json)


query()
