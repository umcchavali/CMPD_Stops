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

## Box plot
chart2 = alt.Chart(traffic).mark_boxplot().encode(
    x = alt.X('Was_a_Search_Conducted'),
    y = alt.Y('Driver_Age')
).properties(
    width = 500,
    title = 'Boxplot between Search Conducted vs Driver Age')

st.altair_chart(chart2)