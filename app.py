import streamlit as st
from utils import extract_text_from_pdf

st.title("🤖 AI Resume Matcher")

# Upload resume
uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

# Job description
job_desc = st.text_area("Paste Job Description")

if uploaded_file and job_desc:
    resume_text = extract_text_from_pdf(uploaded_file)

    st.subheader("📄 Resume Preview")
    st.write(resume_text[:1500])

    # Step 1: Prompt
    prompt = f"""
Compare this resume with the job description.

Resume:
{resume_text}

Job Description:
{job_desc}

Give:
1. Match Score out of 100
2. Missing Skills
3. Improvement Suggestions
"""

    st.subheader("📋 Step 1: Copy this prompt")
    st.text_area("Copy and paste into Claude", prompt, height=200)

    # Step 2: Paste output
    st.subheader("📥 Step 2: Paste Claude Output")
    result = st.text_area("Paste Claude response here", height=200)

    # Step 3: Show result
    if result:
        st.subheader("📊 AI Analysis Result")
        st.success("Analysis Generated Successfully ✅")

        st.write(result)