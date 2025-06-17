import streamlit as st
from parser import extract_text_from_pdf
from skill_extractor import load_skill_list, extract_skills_combined
from ats_scoring import score_resume
from resume_improver import generate_improvement_suggestions  

st.set_page_config(page_title="Resume Matcher", layout="centered")
st.title("🧠 Resume Skill Matcher & ATS Scorer")

uploaded_resume = st.file_uploader("📄 Upload Resume (PDF only)", type=["pdf"])
job_description = st.text_area("📝 Paste the Job Description here")

if uploaded_resume and job_description:
    with st.spinner("Analyzing Resume & Job Description..."):
        skills_db = load_skill_list("skills.json")
        resume_text = extract_text_from_pdf(uploaded_resume)
        resume_skills = set(extract_skills_combined(resume_text, skills_db))
        jd_skills = set(extract_skills_combined(job_description, skills_db))
        matched = resume_skills & jd_skills
        missing = jd_skills - resume_skills
        skill_score = int((len(matched) / len(jd_skills)) * 100) if jd_skills else 0
        total_score, section_presence = score_resume(
            resume_text, jd_skills, resume_skills, list(jd_skills)
        )
        ai_suggestions = generate_improvement_suggestions(
            resume_text, missing, section_presence
        )
    st.subheader("🔍 Skills Match Report")
    st.write(f"✅ **Matching Score:** {skill_score}%")
    st.markdown("**🎯 Skills Matched:**")
    st.success(", ".join(matched) if matched else "No matches found.")
    st.markdown("**⚠️ Missing but Required Skills:**")
    st.error(", ".join(missing) if missing else "None! Great match 🎉")
    st.subheader("📊 ATS Resume Score")
    st.metric("Total ATS Score", f"{total_score} / 100")
    st.subheader("📌 Section Analysis")
    for section, present in section_presence.items():
        if present:
            st.markdown(f"✅ {section.capitalize()}")
        else:
            st.warning(f"⚠️ Missing section: {section.capitalize()}")
    st.subheader("🤖 AI-Powered Resume Suggestions")
    st.code(ai_suggestions, language="markdown")
    st.download_button("📥 Download Suggestions",
                       ai_suggestions,
                       file_name="resume_suggestions.txt",
                       mime="text/plain")
