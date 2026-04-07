# 🚀 AI Resume Matcher (Auto AI Version)

An AI-powered web application that analyzes resumes against job descriptions and provides a match score, skill gap analysis, and actionable improvement suggestions.

---

## 🌐 Live Demo
👉 https://ai-resume-matcher-js.streamlit.app

---

## 📸 App Preview

![App Screenshot](screenshot.png)

---

## 🔍 Features

- 📄 Upload Resume (PDF)
- 📝 Paste Job Description
- 🎯 AI-based Match Score (0–100)
- ❌ Missing Skills Identification
- ✅ Strengths Detection
- 💡 Personalized Resume Suggestions
- 📊 Clean and Interactive UI

---

## ⚙️ Tech Stack

- Python
- Streamlit
- OpenAI API
- PDFPlumber

---

## 🧠 How It Works

1. Extracts text from uploaded resume (PDF)
2. Combines resume content with job description
3. Sends structured prompt to OpenAI
4. AI analyzes alignment and returns:
   - Match Score
   - Missing Skills
   - Strengths
   - Suggestions

---

## 🚀 Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
