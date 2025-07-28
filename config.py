# config.py

API_KEY = "AIzaSyArAEub-AaeJBLWGtsnup-8ngj4HUkGGBs"
ENDPOINT = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"
LANGFUSE_BASE_URL = "https://cloud.langfuse.com"
LANGFUSE_SECRET_KEY = "sk-lf-aaa50ee2-d70b-4bb5-82b1-9abdaa6746d9"
LANGFUSE_PUBLIC_KEY = "pk-lf-1dec998f-3eb1-437a-b588-4b35f5a89f66"
from langfuse import Langfuse

langfuse = Langfuse(
    secret_key="sk-lf-aaa50ee2-d70b-4bb5-82b1-9abdaa6746d9",
    public_key="pk-lf-1dec998f-3eb1-437a-b588-4b35f5a89f66",
    host="https://cloud.langfuse.com",
)
