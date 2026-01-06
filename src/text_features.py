from sklearn.feature_extraction.text import TfidfVectorizer

def build_tfidf_features(urls):
    vectorizer = TfidfVectorizer(
        lowercase=True,
        ngram_range=(1,2),
        max_features=5000,
        token_pattern=r"[a-zA-Z0-9]+"
    )
    X = vectorizer.fit_transform(urls)
    return X, vectorizer