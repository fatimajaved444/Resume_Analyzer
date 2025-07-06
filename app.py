import streamlit as st
from modules.matcher import compute_match_score
from modules.strengths import extract_strengths
from modules.weaknesses import detect_weaknesses
from modules.course_recommender import recommend_courses
from modules.profession_predictor import suggest_profession
from modules.ats_checker import check_ats_compatibility
import re 
from PyPDF2 import PdfReader
import docx2txt
import pandas as pd
import os
st.set_page_config(page_title="AI Resume Analyzer", layout="wide")
st.title("🤖 AI Resume Analyzer (ML Powered)")

# File reading helper
def read_file(file):
    if file.name.endswith(".pdf"):
        reader = PdfReader(file)
        return " ".join([page.extract_text() or "" for page in reader.pages])
    elif file.name.endswith(".docx"):
        return docx2txt.process(file)
    elif file.name.endswith(".txt"):
        return file.read().decode("utf-8")
    return ""
# --- Resume Analysis ---
def extract_contact_details(text):
    email = re.findall(r"[\w\.-]+@[\w\.-]+", text)
    phone = re.findall(r"(?:\+?\d{1,3}[-.\s]?)?(?:\(?\d{3}\)?[-.\s]?){1,2}\d{4}", text)
    name = " ".join(text.split()[:2])
    return {
        "name": name,
        "email": email[0] if email else "Not Found",
        "phone": phone[0] if phone else "Not Found"
    }
    
# Sidebar - Inputs
with st.sidebar:
   
    st.header("📄 Job Description Input Method")
    jd_input_type = st.radio("Select Job Description Input", ["Upload File", "Paste Text"])

    jd_file = None
    jd_text_input = ""

    if jd_input_type == "Upload File":
        jd_file = st.file_uploader("Upload JD File", type=["pdf", "docx", "txt"])
    else:
        jd_text_input = st.text_area("Paste Job Description")
    st.header("📄 Upload Resume")
    resume_file = st.file_uploader("Upload Resume", type=["pdf", "docx"])


    analyze = st.button("🚀 Analyze")

# Analysis Trigger
if analyze:
    if not resume_file:
        st.error("Please upload your resume.")
    else:
        # Read Resume
        resume_text = read_file(resume_file)
        contact_details = extract_contact_details(resume_text)
        # Read JD text
        if jd_input_type == "Upload File" and jd_file:
            jd_text = read_file(jd_file)
        elif jd_input_type == "Paste Text" and jd_text_input.strip():
            jd_text = jd_text_input.strip()
        else:
            jd_text = ""

        if not jd_text:
            st.error("Please provide a job description via selected input method.")
        else:
            st.subheader("👤 Candidate Details:")
            st.write(f"**Name:** {contact_details['name']}")
            st.write(f"**Email:** {contact_details['email']}")
            st.write(f"**Phone:** {contact_details['phone']}")
            st.subheader("📊 Resume-JD Match Score")
            score = compute_match_score(jd_text, resume_text)
            st.progress(int(score))
            st.success(f"Match Score: **{score:.2f}%**")

            strengths = extract_strengths(jd_text, resume_text)
            weaknesses = detect_weaknesses(jd_text, resume_text)

            st.subheader("💪 Strengths (Matched Skills)")
            st.write(strengths or "No strong matches found.")

            st.subheader("⚠️ Weaknesses (Missing from Resume)")
            st.write(weaknesses or "No obvious weaknesses found.")

            st.subheader("🎓 Course Recommendations")
            course_recs = recommend_courses(weaknesses)
            if course_recs:
                for skill, course in course_recs:
                    st.markdown(f"- **{skill.capitalize()}**: {course}")
            else:
                st.write("No course suggestions needed. You're well-aligned!")

            st.subheader("🧠 Suitable Profession Suggestion")
            profession = suggest_profession(resume_text)
            st.success(f"Best-fit profession: **{profession}**")

            st.subheader("📄 ATS Compatibility Check")
            ats_friendly, tips = check_ats_compatibility(resume_text)
            if ats_friendly:
                st.success("✅ ATS Friendly Resume")
            else:
                st.warning("⚠️ Resume needs improvements for ATS compatibility")
                for tip in tips:
                    st.markdown(f"- {tip}")
            # Log Results
        log_data = {
            "Name": contact_details["name"],
            "Email": contact_details["email"],
            "Phone": contact_details["phone"],
            "Match Score": round(score,2),
            "Suggested Profession": profession,
            "Strengths": ", ".join(strengths) if strengths else "None",
            "Weaknesses": ", ".join(weaknesses) if weaknesses else "None",
            "ATS Compatible": "Yes" if ats_friendly else "No"
        }

        log_df = pd.DataFrame([log_data])

        if os.path.exists("admin_log.csv"):
            log_df.to_csv("admin_log.csv", mode='a', index=False, header=False)
        else:
            log_df.to_csv("admin_log.csv", index=False)
else:
    st.info("Please upload your resume and job description, then click 'Analyze'.")
