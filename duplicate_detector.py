import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def detect_duplicates(questions, threshold=0.85):
    """
    Scikit-learn TF-IDF + Cosine Similarity Duplicate Detector
    Detects exact and near-duplicate question stems across the dataset.
    Returns a list of duplicate pairs found.
    """
    if not questions:
        return []

    texts = [q["question"].lower().strip() for q in questions]
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(texts)
    similarity_matrix = cosine_similarity(tfidf_matrix)

    duplicates = []
    num_questions = len(questions)

    for i in range(num_questions):
        for j in range(i + 1, num_questions):
            sim = similarity_matrix[i, j]
            # Check for high similarity or exact match
            if sim >= threshold or texts[i] == texts[j]:
                duplicates.append({
                    "sim_score": round(float(sim), 4),
                    "q1_id": questions[i].get("question_id"),
                    "q1_role": questions[i].get("role"),
                    "q1_text": questions[i].get("question"),
                    "q2_id": questions[j].get("question_id"),
                    "q2_role": questions[j].get("role"),
                    "q2_text": questions[j].get("question")
                })

    return duplicates
