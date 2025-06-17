import json
import spacy
from rapidfuzz import fuzz
nlp = spacy.load("en_core_web_md")

def load_skill_list(path="skills.json"):
    with open(path, "r") as file:
        data = json.load(file)
    return data 
def extract_skills_from_text_fuzzy(text, skill_list, threshold=85):
    found_skills = set()
    text_lower = text.lower()
    for skill in skill_list:
        for word in text_lower.split():
            if fuzz.partial_ratio(skill.lower(), word) >= threshold:
                found_skills.add(skill)
                break
    return list(found_skills)

def extract_skills_nlp(text, skill_list, threshold=0.75):
    doc = nlp(text.lower())
    found_skills = set()
    for skill in skill_list:
        skill_doc = nlp(skill.lower())
        for token in doc:
            if token.has_vector and skill_doc.has_vector:
                similarity = token.similarity(skill_doc)
                if similarity >= threshold:
                    found_skills.add(skill)
                    break
    return list(found_skills)

def extract_skills_combined(text, skill_list):
    fuzzy = set(extract_skills_from_text_fuzzy(text, skill_list))
    nlp_based = set(extract_skills_nlp(text, skill_list))
    return list(fuzzy | nlp_based)
