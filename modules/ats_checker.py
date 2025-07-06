
import re

def check_ats_compatibility(resume_text):
    tips = []
    ats_friendly = True

    if not re.search(r'\bexperience\b', resume_text, re.IGNORECASE):
        tips.append("Include a dedicated 'Experience' section.")
        ats_friendly = False
    if re.search(r'\.(jpg|png)', resume_text, re.IGNORECASE):
        tips.append("Remove images or icons – ATS bots can't read them.")
        ats_friendly = False
    if len(resume_text.split()) < 150:
        tips.append("Your resume is too short to provide detailed ATS context.")
        ats_friendly = False

    return ats_friendly, tips
