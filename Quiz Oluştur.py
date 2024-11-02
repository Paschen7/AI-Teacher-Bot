import io
import streamlit as st
import time as ts
import chat
import re
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics


im = Image.open('robot-icon.png')
st.set_page_config(page_title="Quiz Oluştur", page_icon=im)

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

left_column, middle_column ,right_column = st.columns(3)
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

with middle_column:
    if lesson == 'Matematik':
        multi_select = st.multiselect("Hangi konu", options=mathematics_lessons)
    elif lesson == 'Fizik':
        multi_select = st.multiselect("Hangi konu", options=physics_lessons)
    elif lesson == 'Kimya':
        multi_select = st.multiselect("Hangi konu", options=chemistry_lessons)
    elif lesson == 'Biyoloji':
        multi_select = st.multiselect("Hangi konu", options=biology_lessons)

with right_column:
    difficulty = st.selectbox('Zorluk Seçin',options=('Kolay','Orta','Zor','Çok Zor'))

question = f"Bana {lesson} dersinden {multi_select} konusu üzerine zorluğu {difficulty} olan 20 tane test sorusu verebilir misin? soruların şıkları bir alt satırda olsun, birbirlerine bitişik olmasın, sorular kalın olsun!"


def generate_bot_response(user_input):
    response = chat.chat_session.send_message(user_input)
    model_response = response.text
    model_response = re.sub(r"\*", "", model_response)
    return model_response


def generate_pdf(content):
    buffer = io.BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=letter)
    
    pdfmetrics.registerFont(TTFont("FreeSans", "fonts/FreeSans.ttf"))
    pdf.setFont("FreeSans", 12)
    
    pdf.drawString(100, 750, "Oluşturulan Quiz Soruları")
    y = 720
    
    for line in content.split('\n'):
        if y < 40:
            pdf.showPage()
            pdf.setFont("FreeSans", 12)
            y = 750
        pdf.drawString(30, y, line)
        y -= 20
    
    pdf.save()
    buffer.seek(0)
    return buffer


st.markdown("""
<style>
    .stButton {
        text-align: center;
        margin: auto;
    }
</style>
""", unsafe_allow_html=True)


if st.button("Soruları Getir", type="primary"):
    if not multi_select:
        st.warning("Lütfen en az bir konu seçin!")
    else:
        response = generate_bot_response(question)

        pdf_buffer = generate_pdf(response)
        st.download_button(
            label="Soruları PDF olarak indir",
            data=pdf_buffer,
            file_name="quiz_sorulari.pdf",
            mime="application/pdf"
        )
