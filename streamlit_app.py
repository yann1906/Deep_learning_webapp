import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

DATA = pd.read_csv('ETHUSDT_data.csv')
st.subheader('Raw data')
st.write(DATA)
