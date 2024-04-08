import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
st.header("Bar Graph")

@st.cache_data
def load_data(csv):
    df = pd.read_csv(csv)
    return df

traffic = load_data("data/Officer_Traffic_Stops.csv")

## Histogram
age_bar = alt.Chart(traffic).mark_bar().encode(
    alt.X("Driver_Age:Q", bin=alt.BinParams(maxbins=50)),
    y='count()',
).properties(width=800,height=400)

st.altair_chart(age_bar)