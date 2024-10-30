import streamlit as st
import time as ts
import pandas as pd
import numpy as np
import chat
import re
from PIL import Image


im = Image.open('robot-icon.png')
st.set_page_config(page_title="Quiz Değerlendir", page_icon = im)
st.write("Yüklediğiniz quiz sonuçlarından öğrencilerin performansını ve soru istatistiklerini analiz edebilirsiniz.")
st.markdown("""
 <style>
     .css-1rs6os {
            visibility: hidden;
     }
     .css-1lsmgbg 
                 {
                     visibility: hidden;
                 }  
 </style>
 """, unsafe_allow_html=True)

st.markdown("""
<div style="text-align:center">
    <h1>Quiz Değerlendir</h1>
    <hr></hr>
    <br></br>
</div>
""", unsafe_allow_html=True)

# PDF yükleme alanı
uploaded_files = st.file_uploader("Quiz sonuçlarını içeren PDF dosyalarını yükleyin", accept_multiple_files=True, type="pdf")

