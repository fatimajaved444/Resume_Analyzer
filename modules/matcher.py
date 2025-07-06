
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')

def compute_match_score(jd_text, resume_text):
    jd_vec = model.encode([jd_text])[0]
    res_vec = model.encode([resume_text])[0]
    return float(cosine_similarity([jd_vec], [res_vec])[0][0]) * 100
