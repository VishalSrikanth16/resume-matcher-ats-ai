import re

def extract_sections(text):
    sections = {
        "summary": bool(re.search(r"\bsummary\b", text, re.IGNORECASE)),
        "experience": bool(re.search(r"\bexperience\b|\bemployment\b|\bwork history\b", text, re.IGNORECASE)),
        "education": bool(re.search(r"\beducation\b", text, re.IGNORECASE)),
        "projects": bool(re.search(r"\bprojects?\b", text, re.IGNORECASE)),
        "contact": bool(re.search(r"\b(email|phone|contact|linkedin|github)\b", text, re.IGNORECASE)),
    }
    return sections

def score_resume(text, jd_skills, resume_skills, keywords=None):
    total_score = 0
    skill_overlap = resume_skills & jd_skills
    skill_score = (len(skill_overlap) / len(jd_skills)) * 30 if jd_skills else 0
    total_score += skill_score
    keyword_score = 0
    if keywords:
        matched_keywords = [k for k in keywords if k.lower() in text.lower()]
        keyword_score = min(len(matched_keywords), 10) * 2  
        total_score += keyword_score
    exp_match = re.search(r'(\d+)\+?\s+years?.+experience', text, re.IGNORECASE)
    if exp_match:
        years = int(exp_match.group(1))
        if years >= 3:
            total_score += 15
        elif years >= 1:
            total_score += 10
        else:
            total_score += 5
    if re.search(r"(bachelor|master|b\.tech|bsc|msc|bca|mca)", text, re.IGNORECASE):
        total_score += 10
    soft_skills = [
        "communication", "teamwork", "problem-solving", "leadership",
        "critical thinking", "adaptability", "collaboration", "creativity"
    ]
    soft_count = sum(1 for s in soft_skills if s.lower() in text.lower())
    soft_score = min(soft_count * 1.5, 10)  
    total_score += soft_score
    lines = text.split("\n")
    avg_line_length = sum(len(line.strip()) for line in lines if line.strip()) / max(len(lines), 1)
    if 40 <= avg_line_length <= 120:
        total_score += 5
    sections = extract_sections(text)
    section_score = sum(2 for v in sections.values() if v) 
    total_score += section_score
    
    return round(total_score), sections
