import streamlit as st
import pandas as pd
import numpy as np
st.write("Test")
st.write('Micah Richardson was here!')
@st.cache_data(5)
def load_data(csv):
    df = pd.read_csv(csv)
    return df
traffic = load_data("data/Officer_Traffic_Stops.csv")
st.dataframe(traffic)