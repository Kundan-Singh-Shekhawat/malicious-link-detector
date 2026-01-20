# Malicious Link Detector (Deployed)

This project explores detecting malicious or phishing URLs using machine learning.

## 🔗 Live Deployment (Swagger UI)

The API is publicly deployed on AWS EC2 and can be accessed here:

👉 http://3.110.213.9:8000/docs

You can use this Swagger UI to test the `/predict` endpoint with real URLs.

## Current Status

- Dataset loading and exploration
- Understanding class distribution and basic URL characteristics

## Dataset

The dataset contains URLs labeled as benign or malicious and is used for supervised learning experiments.

## Next Steps

- Feature engineering on URLs (keywords, structure)
- Baseline ML model training


## Baseline Model Results (Keyword + Structural Features)

A Logistic Regression model was trained using basic URL features such as length, digit count, special character count, and suspicious keyword presence.

**Test Set Performance:**
- Accuracy: ~72%
- Precision (Malicious): ~83%
- Recall (Malicious): ~47%

**Observations:**
- The model detects obvious malicious URLs with high precision.
- Recall for malicious URLs is low, indicating many subtle phishing links are missed.
- This highlights the limitation of keyword-based features and motivates more expressive text-based features.

## TF-IDF Model Results (v2)

A TF-IDF based Logistic Regression model was trained to capture statistical patterns in URLs beyond hand-crafted keywords.

**Test Set Performance:**
- Accuracy: ~93%
- Precision (Malicious): ~91%
- Recall (Malicious): ~92%

**Comparison with Baseline:**
- Significant improvement in recall for malicious URLs
- Better detection of subtle phishing links
- Confirms limitations of keyword-only approaches
# Malicious Link Detector

This project implements a machine learning–based **malicious URL detection system** and exposes it as a **REST API using FastAPI**.  
The system analyzes URLs, extracts handcrafted features, and predicts the probability that a link is malicious (phishing, scam, or harmful).

The trained model is served as an **inference service**, containerized with **Docker**, and designed for deployment.

---

## System Architecture

The system follows a clear, production-oriented flow:

```
URL → Feature Extraction → ML Model → Probability → Decision
```

1. A client sends a URL to the API  
2. The API extracts numerical features from the URL  
3. A trained ML model predicts malicious probability  
4. A configurable threshold determines the final decision  
5. The API returns the probability and classification  

---

## Dataset

The dataset contains URLs labeled as **benign** or **malicious**, used for supervised learning.

The data is used only for **offline training**.  
The deployed service performs **inference only**.

---

## Feature Engineering

Handcrafted URL-based features are extracted, including:

- URL length
- Number of digits
- Number of special characters
- Suspicious keyword presence
- Structural URL patterns

Feature names are **persisted during training** to ensure strict schema consistency between training and inference, preventing deployment-time errors.

---

## Model Details

- Model: Logistic Regression  
- Input: Handcrafted URL features  
- Output: Probability of a URL being malicious  
- Decision Logic: Threshold-based classification  

The model is trained offline and loaded **once at API startup** for efficient inference.

---

## Baseline Model Results (Keyword + Structural Features)

A Logistic Regression model trained on basic handcrafted URL features.

**Test Set Performance:**
- Accuracy: ~72%
- Precision (Malicious): ~83%
- Recall (Malicious): ~47%

**Observations:**
- High precision on obvious malicious URLs  
- Low recall for subtle phishing links  
- Demonstrates limitations of keyword-only features  

---

## TF-IDF Model Results

A TF-IDF–based Logistic Regression model capturing richer URL patterns.

**Test Set Performance:**
- Accuracy: ~93%
- Precision (Malicious): ~91%
- Recall (Malicious): ~92%

**Key Improvements:**
- Strong recall on subtle phishing URLs  
- Better generalization beyond handcrafted keywords  

---

## API Usage

### Health Check

```
GET /
```

Response:
```json
{
  "status": "Malicious link detection service is running"
}
```

---

### Predict Malicious URL

```
POST /predict
```

Request body:
```json
{
  "url": "https://example.com/login"
}
```

Response:
```json
{
  "malicious_probability": 0.384,
  "decision": "benign"
}
```

---

## Running Locally (FastAPI)

1. Create and activate a virtual environment  
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Start the API:
   ```
   uvicorn app:app --reload
   ```
4. Open Swagger UI:
   ```
   http://127.0.0.1:8000/docs
   ```

---

## Running with Docker

Build the Docker image:
```
docker build -t malicious-link-detector .
```

Run the container:
```
docker run -p 8000:8000 malicious-link-detector
```

Access the API:
```
http://localhost:8000/docs
```

---

## Limitations

- Dataset may not capture evolving phishing tactics  
- Relies on handcrafted features rather than deep learning  
- Performance depends on feature engineering quality  

These limitations provide clear scope for future work.

---

## Future Improvements

- Character-level or deep learning–based models  
- Rate limiting and authentication  
- Cloud deployment on AWS  
- Continuous retraining with fresh data  

---

## Project Status

✔ Model training completed  
✔ FastAPI inference service implemented  
✔ Docker containerization completed  
✔ Deployed on AWS EC2 (public API)

--- END NEW README CONTENT ---