import pandas as pd

# Load course data
courses_df = pd.read_csv("data/courses.csv")

# Normalize skill column
courses_df['skill'] = courses_df['skill'].str.lower().str.replace("-", " ").str.strip()

def recommend_courses(weak_skills):
    # Normalize incoming weak skills
    normalized_weak_skills = [skill.lower().replace("-", " ").strip() for skill in weak_skills]

    # Filter matching skills
    recommendations = courses_df[courses_df['skill'].isin(normalized_weak_skills)]

    return recommendations[['skill', 'course']].drop_duplicates().values.tolist()
