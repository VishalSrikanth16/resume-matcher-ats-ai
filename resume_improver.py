import requests

COHERE_API_KEY = "your_api_key"
API_URL = "https://api.cohere.ai/v1/generate"
HEADERS = {
    "Authorization": f"Bearer {COHERE_API_KEY}",
    "Content-Type": "application/json"
}
def generate_improvement_suggestions(resume_text, missing_skills, missing_sections):
    prompt = f"""
You are an expert in resume improvement. Given the following resume, provide 3 specific and actionable suggestions to improve it.
Resume:
{resume_text}

Missing Skills: {', '.join(missing_skills)}
Missing Sections: {', '.join([section for section, present in missing_sections.items() if not present])}
Suggestions:
"""
    payload = {
        "model": "command",  
        "prompt": prompt,
        "max_tokens": 300,
        "temperature": 0.7
    }
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    if response.status_code == 200:
        return response.json().get("generations")[0].get("text", "❌ No suggestions returned.")
    else:
        return f"❌ Cohere API error {response.status_code}: {response.text}"
