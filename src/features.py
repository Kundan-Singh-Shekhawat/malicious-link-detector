import re

SUSPICIOUS_KEYWORDS = [
    "login", "verify", "secure",
    "account", "update", "confirm"
]

def extract_features(url: str) -> dict:
    url = url.lower()

    features = {
        "url_length": len(url),
        "num_digits": sum(char.isdigit() for char in url),
        "num_special_chars": len(re.findall(r"[-@?=]", url)),
        "keyword_count": sum(1 for word in SUSPICIOUS_KEYWORDS if word in url)
    }

    return features
# Example usage
# if __name__ == "__main__":
#     test_url = "http://example.com/verify-account?user=123"
#     features = extract_features(test_url)
#     print(features)