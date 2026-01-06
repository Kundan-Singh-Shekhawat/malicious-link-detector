import sys
import os
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))

from src.text_features import build_tfidf_features

# Load dataset 
df = pd.read_csv("data/urls.csv")

X, vectorizer = build_tfidf_features(df["url"])
y = df["label"]

X_train,X_test,y_train,y_test = train_test_split(
    X,y, test_size=0.2, random_state=42, stratify=y
)

model = LogisticRegression(max_iter=1000)
model.fit(X_train,y_train)

y_pred = model.predict(X_test)

print("TF-IDF Model Results:")
print(classification_report(y_test, y_pred))