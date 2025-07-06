
from transformers import pipeline

classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

CANDIDATE_PROFESSIONS = ["Data Scientist", "ML Engineer", "Cloud Engineer", "Software Developer", "Business Analyst"]

def suggest_profession(resume_text):
    result = classifier(resume_text, CANDIDATE_PROFESSIONS)
    return result["labels"][0]
