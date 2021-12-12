import streamlit as st
import numpy as np
import pandas as pd
import zipfile

zf = zipfile.ZipFile('https://github.com/yann1906/Deep_learning_webapp/blob/main/ETHUSDT_data.zip') 
zf.namelist() 
# df = pd.read_csv(zf.open('intfile.csv'))

# DATA = pd.read_csv('ETHUSDT_data.csv')
# st.subheader('Raw data')
# st.write(DATA)
