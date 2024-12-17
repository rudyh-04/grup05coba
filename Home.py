import pandas as pd
import matplotlib as plt
import numpy as np
import streamlit as st
from PIL import Image

st.title('Welcome')
st.image('Pentachem.jpg')

st.header('Absensi')
st.subheader('Tetap semangat')

st.subheader('Supply Chain Departement')
st.subheader('Cikarang Plant')


st.sidebar.header('Feedback')

option = st.sidebar.selectbox(
    'Please Select',
    ('Good', 'Not Good','Observation')
)
option = st.sidebar.button('save')



