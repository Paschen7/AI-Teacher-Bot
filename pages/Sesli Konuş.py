import streamlit as st
import time as ts
import chat
import re
from PIL import Image
import speech_recognition as sr
import API
from voice import text_to_speech

im = Image.open('robot-icon.png')
st.set_page_config(page_title="Sesli Konuş", page_icon=im)

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

st.markdown("""
<style>
    .stButton {
        text-align: center;
        margin: auto;
    }
</style>
""", unsafe_allow_html=True)


def generate_bot_response(user_input):
    response = chat.chat_session.send_message(user_input)
    model_response = response.text
    model_response = re.sub(r"\*", "", model_response)

    return model_response


recognizer = sr.Recognizer()

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


def speak():
    text_to_speech("Merhaba, nasıl yardımcı olabilirim", API.eleven_labs_api)

    while True:
        with sr.Microphone() as source:
            audio = recognizer.listen(source)
            try:
                text = recognizer.recognize_google(audio, language='tr-TR')
                st.write("Siz: ", text)

            except sr.UnknownValueError:
                st.write("Sesi Anlyamadım")

            except sr.RequestError as e:
                st.write("Servis Hatası")

        if text == "Görüşürüz" or text == "görüşürüz":
            text_to_speech("Görüşürüz bir şey sormak istersen her zaman burdayım", API.eleven_labs_api)
            break

        response = chat.chat_session.send_message(text)

        model_response = response.text
        model_response = re.sub(r"\*", "", model_response)

        text_to_speech(model_response, API.eleven_labs_api)
        st.write("Bot: ", model_response)


if st.button("Konuşmaya Başla", type="primary"):
    speak()
