from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

df = pd.DataFrame(
    np.random.randn(50, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(df)  # Same as st.write(df)
st.markdown('Streamlit is **_really_ cool**.')
