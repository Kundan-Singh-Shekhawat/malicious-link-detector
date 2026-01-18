from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

from src.features import extract_features

app = FastAPI(title="Malicious Link Detector")

model = joblib.load("models/malicious_link_model.joblib")
feature_names = joblib.load("models/feature_names.joblib")
THRESHOLD = 0.6

class LinkInput(BaseModel):
    url:str

@app.get("/")
def root():
    return {"status": "Malicious link detection service is running"}

@app.post("/predict")
def predict(input: LinkInput):
    feature_dict = extract_features(input.url)
    df = pd.DataFrame([feature_dict],columns=feature_names)
    prob = model.predict_proba(df)[0][1]
    decision = "malicious" if prob>= THRESHOLD else "genign"

    return {
        "malicious_probability": round(float(prob),3),
        "decision": decision
    }