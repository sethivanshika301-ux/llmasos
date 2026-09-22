import os
from dotenv import load_dotenv

def get_openai_api_key():
    load_dotenv()  # Load environment variables from .env file
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in environment variables.")
    return api_key