import streamlit as st
import time as ts
import chat
import re


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
 """, unsafe_allow_html = True)

st.markdown("""
<div style="text-align:center">
    <h1>Quiz Üret</h1>
    <hr></hr>
    <br></br>
</div>
""", unsafe_allow_html=True)

left_column, right_column = st.columns(2)
with left_column:
    lesson = st.selectbox("Quiz yapmak istediğiniz dersi seçiniz", options = ('Matematik', 'Fizik', 'Kimya', 'Biyoloji'))

mathematics_lessons = ["Üslü ve köklü sayılar", "Mutlak değer", "Eşitsizlikler", "Problemler", "Geometri", "Analitik geometri", "Olasılık", "Fonksiyonlar", "Limit ve süreklilik", "Türev", "İntegral", "Trigonemetri"]
physics_lessons = ["Fizik Bilimine Giriş", "Kuvvet ve Hareket", "İş, Enerji ve Güç", "Basınç", "Sıcaklık ve Isı", "Dalgalar", "İtme ve Momentum", "Basit Harmonik Hareketler", "Elektrik ve Manyetizma", "Optik", "Modern Fizik"]
chemistry_lessons = ["Periyodik Sistem", "Kimyasal Bağlar", "Kimyasal Tepimeler", "Asitler, Bazlar ve Tuzlar", "Modern Atom Teorisi", "Maddenin Halleri", "Organik Kimya"]
biology_lessons = ["Canlıların Ortak Özellikleri", "Canlıların Temel Bileşenleri", "Hücre Geçişleri", "Madde Geçişleri", "Canlıların Sınıflandırılması", "Hücre Bölünmeleri ve Üreme", "Kalıtım", "Sistemler","Ekosistem ve Ekoloji", "Bitkiler Biyolojisi", "Genetik", "Ekoloji", "Solunum"]

with right_column:
    if lesson == 'Matematik':
        multi_select = st.multiselect("Hangi konu?", options = mathematics_lessons)
    elif lesson == 'Fizik':
        multi_select = st.multiselect("Hangi konu?", options = physics_lessons)
    elif lesson == 'Kimya':
        multi_select = st.multiselect("Hangi konu?", options = chemistry_lessons)
    elif lesson == 'Biyoloji':
        multi_select = st.multiselect("Hangi konu?", options = biology_lessons)

def generate_bot_response(user_input):
    response = chat.chat_session.send_message(user_input)
    model_response = response.text
    model_response = re.sub(r"\*", "", model_response)

    return model_response

question = f"Bana {lesson} dersinden {multi_select} konusu üzerine 20 tane test sorusu verebilir misin? soruların şıkları bir alt satırda olsun, birbirlerine bitişik olmasın, sorular kalın olsun ve cevap anahtarı da olsun istiyorum"

st.markdown("""
<style>
    .stButton {
        text-align: center;
        margin: auto;
    }
</style>
""", unsafe_allow_html=True)


if st.button("Soruları Getir"):
    response = generate_bot_response(question)
    st.write(response)

# with st.container():
#     col1, col2, col3 = st.columns([8, 4, 8])
#     with col2:
#         st.button("Soruları Getir!")
#
# if col2:
#     response = generate_bot_response(question)
#     st.write(response)

########################################
# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []
#
# user_input = st.text_input("Sormak istediğiniz soruyu yazınız? ")
#
# if user_input:
#     st.session_state.chat_history.append({"user": user_input})
#
#     bot_response = generate_bot_response(user_input)
#     st.session_state.chat_history.append({"bot": bot_response})
#
# st.write("### Sohbet Geçmişi")
# for message in st.session_state.chat_history:
#     if "user" in message:
#         st.write(f"**Kullanıcı:** {message['user']}")
#     elif "bot" in message:
#         st.write(f"**Chatbot:** {message['bot']}")
###################################################




