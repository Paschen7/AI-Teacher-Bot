import streamlit as st
import time as ts
import chat
import re
from PIL import Image

im = Image.open('robot-icon.png')
st.set_page_config(page_title="Sesli Konuş", page_icon = im)

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
    <h1>Sesli Konuş</h1>
    <hr></hr>
    <br></br>
</div>
""", unsafe_allow_html=True)