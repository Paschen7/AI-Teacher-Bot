import streamlit as st
import time as ts
import chat
import re
from PIL import Image

im = Image.open('robot-icon.png')
st.set_page_config(page_title="Quiz Oluştur", page_icon = im)

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
    <h1>Quiz Üret</h1>
    <hr></hr>
    <br></br>
</div>
""", unsafe_allow_html=True)

left_column, right_column = st.columns(2)
with left_column:
    lesson = st.selectbox("Quiz yapmak istediğiniz dersi seçiniz", options=('Matematik', 'Fizik', 'Kimya', 'Biyoloji'))

mathematics_lessons = ["Üslü ve köklü sayılar", "Mutlak değer", "Eşitsizlikler", "Problemler", "Geometri",
                       "Analitik geometri", "Olasılık", "Fonksiyonlar", "Limit ve süreklilik", "Türev", "İntegral",
                       "Trigonemetri"]
physics_lessons = ["Fizik Bilimine Giriş", "Kuvvet ve Hareket", "İş, Enerji ve Güç", "Basınç", "Sıcaklık ve Isı",
                   "Dalgalar", "İtme ve Momentum", "Basit Harmonik Hareketler", "Elektrik ve Manyetizma", "Optik",
                   "Modern Fizik"]
chemistry_lessons = ["Periyodik Sistem", "Kimyasal Bağlar", "Kimyasal Tepimeler", "Asitler, Bazlar ve Tuzlar",
                     "Modern Atom Teorisi", "Maddenin Halleri", "Organik Kimya"]
biology_lessons = ["Canlıların Ortak Özellikleri", "Canlıların Temel Bileşenleri", "Hücre Geçişleri", "Madde Geçişleri",
                   "Canlıların Sınıflandırılması", "Hücre Bölünmeleri ve Üreme", "Kalıtım", "Sistemler",
                   "Ekosistem ve Ekoloji", "Bitkiler Biyolojisi", "Genetik", "Ekoloji", "Solunum"]

with right_column:
    if lesson == 'Matematik':
        multi_select = st.multiselect("Hangi konu", options=mathematics_lessons)
    elif lesson == 'Fizik':
        multi_select = st.multiselect("Hangi konu", options=physics_lessons)
    elif lesson == 'Kimya':
        multi_select = st.multiselect("Hangi konu", options=chemistry_lessons)
    elif lesson == 'Biyoloji':
        multi_select = st.multiselect("Hangi konu", options=biology_lessons)


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

# st.markdown("""
#     <style>
#     .custom-button {
#         background-color: blue;
#         color: white;
#         border: none;
#         padding: 10px 20px;
#         text-align: center;
#         text-decoration: none;
#         display: inline-block;
#         font-size: 16px;
#         margin: 4px 2px;
#         cursor: pointer;
#         border-radius: 5px;
#         transition: background-color 0.3s;
#     }
#
#     .custom-button:hover {
#         background-color: green;
#     }
#     </style>
# """, unsafe_allow_html=True)

# if st.markdown('<button class="custom-button">Soruları Getir</button>', unsafe_allow_html=True):

if st.button("Soruları Getir", type = "primary"):
    if not multi_select:
        st.warning("Lütfen en az bir konu seçin!")
    else:
        response = generate_bot_response(question)
        st.write(response)
