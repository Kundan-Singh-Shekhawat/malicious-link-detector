from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from urllib.parse import urlparse
import joblib
import pandas as pd

from src.features import extract_features

app = FastAPI(title="Malicious Link Detector")

model = joblib.load("models/malicious_link_model.joblib")
feature_names = joblib.load("models/feature_names.joblib")
THRESHOLD = 0.6

def is_valid_url(url: str) -> bool:
    parsed = urlparse(url)

    if parsed.scheme not in ("http", "https"):
        return False

    if not parsed.netloc:
        return False

    if "." not in parsed.netloc:
        return False

    return True

class LinkInput(BaseModel):
    url:str

@app.get("/")
def root():
    return {"status": "Malicious link detection service is running"}

@app.post("/predict")
def predict(input: LinkInput):
    if not is_valid_url(input.url):
        raise HTTPException(
            status_code=400,
            detail="Invalid URL format. Please provide a valid http or https URL."
        )
    feature_dict = extract_features(input.url)
    df = pd.DataFrame([feature_dict],columns=feature_names)
    prob = model.predict_proba(df)[0][1]
    decision = "malicious" if prob>= THRESHOLD else "benign"

    return {
        "malicious_probability": round(float(prob),3),
        "decision": decision
    }