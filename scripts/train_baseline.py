import sys
import os 
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

# Fix import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))

from src.features import extract_features

# Load dataset
df = pd.read_csv("data/urls.csv")

# Build features
X = pd.DataFrame([extract_features(url) for url in df["url"]])
y = df["label"]

# Train-test split
X_train,X_test,y_train,y_test = train_test_split(
    X,y, test_size=0.2, random_state=42, stratify=y
)

# Train baseline model
model = LogisticRegression(max_iter=1000)
model.fit(X_train,y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
print("Confusion Matrix: ")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test,y_pred))
