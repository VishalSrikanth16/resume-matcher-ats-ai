# 🧠 Resume Matcher & ATS Scorer with AI Suggestions

An intelligent AI-powered web application that analyzes your resume against a job description to:
- ✅ Extract relevant skills
- 📊 Score your resume based on ATS (Applicant Tracking System) principles
- 🤖 Generate personalized improvement suggestions using Cohere API

Built with Python, Streamlit, and NLP libraries.

---

## 🚀 Features

- **Resume Skill Matching**: Matches skills from your resume against the job description.
- **ATS Compatibility Score**: Rates your resume out of 100 based on structure, keywords, and completeness.
- **AI-Powered Suggestions**: Uses Cohere to suggest personalized improvements to help your resume stand out.
- **Interactive Web App**: Built with Streamlit for ease of use.

---

## 📂 Project Structure

```
resume_parser/
│
├── app.py # Main Streamlit frontend
├── parser.py # PDF text extractor
├── skill_extractor.py # NLP-based skill extractor
├── ats_scoring.py # ATS-based scoring logic
├── resume_improver.py # AI suggestions using Cohere
├── skills.json # Skill database
├── sample_resumes/ # Sample resumes for testing
└── requirements.txt # Python dependencies
```
---

## 🧪 Try It Out

1. Upload your resume (PDF)
2. Paste a job description
3. View matching score, ATS score, and AI suggestions
4. Improve your resume accordingly 

---

## 📦 Installation

```bash
git clone https://github.com/VishalSrikanth16/resume-matcher-ats-ai.git
cd resume-matcher-ats-ai
pip install -r requirements.txt
```
⚠️ You'll also need a free Cohere API Key
Create a .env file or paste it directly inside resume_improver.py

---

## 🧠 Technologies Used

* Python
* Streamlit
* PyMuPDF for PDF parsing
* NLTK / SpaCy / FuzzyWuzzy for NLP-based skill extraction
* Cohere API for LLM-generated suggestions

## 📄 License
MIT License - feel free to fork and build on top of this!

## 🙌 Acknowledgements
Inspired by the need for smarter job application tools.







