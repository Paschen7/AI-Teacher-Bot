# 🧠 AI-Teacher-Bot

AI-Teacher-Bot is a Streamlit-based web application that helps teachers generate quiz questions and interact with an AI assistant. Leveraging Google's Gemini AI and ElevenLabs for voice output, this project streamlines the process of test creation and AI-powered tutoring.

## 🚀 Features

* 📄 **Custom Quiz Generation**:
  Teachers can select the **subject**, **topic(s)**, and **difficulty level** to generate a set of 20 multiple-choice questions using Gemini AI.

* 📥 **Export to PDF**:
  The generated quiz can be **downloaded as a well-formatted PDF** file directly from the application.

* 🗣️ **AI Conversation with Speech Output**:
  Teachers can **interact with Gemini AI** and listen to its responses via **text-to-speech** using the ElevenLabs API.

* 📚 **Subjects and Topics Supported**:

  * Mathematics
  * Physics
  * Chemistry
  * Biology
    *(Each subject includes a wide range of high-school level topics.)*

## 🛠️ Technologies Used

* **Python 3**
* **Streamlit** for the web interface
* **Google Gemini 1.5 Pro** for generating and analyzing quiz content
* **ElevenLabs Text-to-Speech API** for audio output
* **ReportLab** for PDF generation
* **Pygame** for audio playback

## ⚙️ Setup Instructions

1. **Install required packages**:

   ```bash
   pip install streamlit google-generativeai pygame requests pillow reportlab
   ```

2. **Add your API keys**:

   * Create a file named `API.py` with the following content:

     ```python
     api = "YOUR_GEMINI_API_KEY"
     elevenlabs_api = "YOUR_ELEVENLABS_API_KEY"
     ```

3. **Run the application**:

   ```bash
   streamlit run Quiz_Olustur.py
   ```

## 💡 Future Improvements

* Add student login functionality to save and review quizzes
* Support for more subjects and languages
* Editable question formatting and AI feedback improvements

---
