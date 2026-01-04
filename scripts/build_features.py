import sys
import os
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.features import extract_features

# Load dataset
df = pd.read_csv("data/urls.csv")

# Apply feature extraction
feature_rows = []
for url in df["url"]:
    feature_rows.append(extract_features(url))

# Create feature matrix
X = pd.DataFrame(feature_rows)
y = df["label"]

print("Feature matrix shape:", X.shape)
print("Label vector shape:", y.shape)

print("\nSample features:")
print(X.head())

print("\nSample labels:")
print(y.head())