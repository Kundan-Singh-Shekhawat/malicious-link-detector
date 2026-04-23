# Malicious Link Detector

This project implements a machine learning–based **malicious URL detection system** and exposes it as a **REST API using FastAPI**.  
The system analyzes URLs, extracts handcrafted features, and predicts the probability that a link is malicious (phishing, scam, or harmful).

The trained model is served as an **inference service** and containerized with **Docker**.

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
- Cloud deployment  
- Continuous retraining with fresh data  

---

## Project Status

✔ Model training completed  
✔ FastAPI inference service implemented  
✔ Docker containerization completed
