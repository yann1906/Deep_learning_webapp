import streamlit as st
import numpy as np
import pandas as pd
import zipfile
from urllib.request import urlopen
from io import BytesIO
from zipfile import ZipFile

URL = 'https://github.com/yann1906/Deep_learning_webapp/blob/main/ETHUSDT_data.zip'

def download_and_unzip(url, extract_to='.'):
    http_response = urlopen(url)
    zipfile = ZipFile(BytesIO(http_response.read()))
    zipfile.extractall(path=extract_to)
    
# zf = zipfile.ZipFile('ETHUSDT_data.csv') 
# zf.namelist() 
# df = pd.read_csv(zf.open('intfile.csv'))

DATA = pd.read_csv('ETHUSDT_data.csv')
st.subheader('Raw data')
st.write(DATA)
