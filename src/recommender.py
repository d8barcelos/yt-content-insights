import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(df, column='title'):
    """
    Calcula similaridade de títulos ou categorias.
    """
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df[column])
    similarity = cosine_similarity(tfidf_matrix, tfidf_matrix)
    return similarity

def recommend_videos(base_title, df, similarity_matrix, top_n=5):
    """
    Retorna vídeos semelhantes com base no título.
    """
    try:
        idx = df[df['title'] == base_title].index[0]
        scores = list(enumerate(similarity_matrix[idx]))
        scores = sorted(scores, key=lambda x: x[1], reverse=True)
        top_indices = [i[0] for i in scores[1:top_n+1]]
        return df.iloc[top_indices]
    except IndexError:
        return pd.DataFrame(columns=['title', 'url', 'time'])
