# type: ignore
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
API_KEY = os.getenv("API_KEY")

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=API_KEY)
__all__ = ["llm"]
