import pandas as pd

df = pd.read_csv("data/urls.csv")

print("First 5 rows:")
print(df.head())

print("\nDataset shape:")
print(df.shape)

print("\nClass distribution:")
print(df["label"].value_counts())

df["url_length"] = df["url"].apply(len)

print("\nURL length stats:")
print(df["url_length"].describe())