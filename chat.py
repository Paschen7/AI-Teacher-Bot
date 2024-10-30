import google.generativeai as genai
import API
import re

genai.configure(api_key=API.api)

generation_config = {
  "temperature": 0,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}
safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_NONE",
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
]

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  safety_settings=safety_settings,
)

chat_session = model.start_chat(
    history=[]
)

# Yeni Fonksiyon: PDF içeriğini alıp doğru/yanlış analizini gerçekleştirmek üzere Gemini'ye gönder
def analyze_pdf_content(pdf_text):
    prompt = f"Bu PDF içeriğindeki işaretli cevapların doğru ve yanlış olup olmadığını analiz et ve her sorunun sonucunu doğru veya yanlış olarak belirt:\n\n{pdf_text}"
    response = chat_session.send_message(prompt)
    return response.text  # Yanıtı metin formatında döndür