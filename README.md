# 🎙️ Lecture Summariser

This project is a simple and effective **Lecture Summarisation Tool** that:

1. **Takes audio input** (recorded lecture or spoken content)
2. **Transcribes it using OpenAI's Whisper** (speech-to-text)
3. **Summarises the transcribed text using DeepSeek API** (text summarisation)

---

## 🚀 Features

- 🎧 Converts lecture audio into accurate text using **Whisper**
- ✂️ Automatically generates concise summaries using **DeepSeek**
- 🧠 Custom prompts can be added for flexible summary styles (e.g., bullet points, Q&A format, etc.)

---

## 📦 Libraries & Tools Used

- [Whisper](https://github.com/openai/whisper) – OpenAI’s speech recognition model
- [DeepSeek API](https://platform.deepseek.com/) – for summarising large blocks of text
- Python 3.8+
- `openai-whisper`, `requests`, and other Python dependencies

---

## 📂 Project Workflow

1. **Input Audio**  
   Upload or record a `.wav`, `.mp3`, or `.m4a` file.

2. **Transcription**  
   The audio is converted to text using Whisper.

3. **Summarisation**  
   The transcribed text is passed to DeepSeek’s API with a custom or default summarisation prompt.

4. **Output**  
   A final concise summary is saved or displayed.

---

## 🛠️ Setup Instructions

1. Clone the repo:
   ```bash
   git clone https://github.com/dishav-preet/lecture-summariser.git
   cd lecture-summariser
