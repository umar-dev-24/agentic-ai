import requests
from config import SAFE_BROWSER_API_KEY


def check_url_with_google_safebrowsing(url_to_check: str):
    endpoint = "https://safebrowsing.googleapis.com/v4/threatMatches:find"

    payload = {
        "client": {"clientId": "agentic-ai-checker", "clientVersion": "1.0"},
        "threatInfo": {
            "threatTypes": [
                "MALWARE",
                "SOCIAL_ENGINEERING",
                "UNWANTED_SOFTWARE",
                "POTENTIALLY_HARMFUL_APPLICATION",
            ],
            "platformTypes": ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [{"url": url_to_check}],
        },
    }

    params = {"key": SAFE_BROWSER_API_KEY}
    response = requests.post(endpoint, params=params, json=payload)
    data = response.json()

    if "matches" in data:
        return False
    else:
        return True


# Example usage:
