def load_technical_skills():
    with open("data/skills.txt", "r") as f:
        return set(line.strip().lower() for line in f)

def extract_strengths(jd_text, resume_text):
    tech_skills = load_technical_skills()
    jd_words = set(jd_text.lower().split())
    resume_words = set(resume_text.lower().split())
    
    matched_skills = tech_skills & jd_words & resume_words
    return list(matched_skills)
