from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def consistency_score(texts):
    """
    Compute how consistent a list of answers are.
    Returns a number between 0 and 1.
    """
    if len(texts) < 2:
        return 1.0
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(texts)
    sim = cosine_similarity(X)
    n = len(sim)
    total = 0
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            total += sim[i][j]
            count += 1
    return total / count if count > 0 else 0
