import streamlit as st
import panda as pd
import numpy as np

DATA = pd.read_csv('ETHUSDT_data.csv')
st.subheader('Raw data')
st.write(DATA)
