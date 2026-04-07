import streamlit as st
from utils import extract_text_from_pdf
from openai import OpenAI
import re

client = OpenAI()

st.set_page_config(page_title="AI Resume Matcher", layout="centered")

st.title("🚀 AI Resume Matcher (Auto AI Version)")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type="pdf")
job_desc = st.text_area("Paste Job Description", height=200)

if uploaded_file and job_desc:
    if st.button("Analyze 🚀"):

        resume_text = extract_text_from_pdf(uploaded_file)

        prompt = f"""
You are an expert ATS system.

Compare the resume and job description.

Return ONLY this format:

Match Score: XX/100

Missing Skills:
- skill 1
- skill 2

Strengths:
- point 1
- point 2

Suggestions:
- suggestion 1
- suggestion 2

RESUME:
{resume_text}

JOB DESCRIPTION:
{job_desc}
"""

        with st.spinner("Analyzing... 🤖"):
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}]
            )

        result = response.choices[0].message.content

        st.success("Analysis Generated Successfully ✅")

        # Extract score
        score = None
        for line in result.split("\n"):
            if "Match Score" in line:
                match = re.search(r"\d+", line)
                if match:
                    score = int(match.group())
                break

        if score:
            score = min(score, 100)
            st.subheader("🎯 Match Score")
            st.metric("Score", f"{score}%")
            st.progress(score / 100)

        st.subheader("🧠 Detailed Insights")
        st.write(result)