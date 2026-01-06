# Malicious URL Detection

This project explores detecting malicious or phishing URLs using machine learning.

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