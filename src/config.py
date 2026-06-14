import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Fetch the API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def validate_environment():
    """Ensures all required environment variables are set before the app runs."""
    if not GEMINI_API_KEY or GEMINI_API_KEY == "your_api_key_here":
        raise ValueError(
            "🚨 GEMINI_API_KEY is missing or invalid. "
            "Please check your .env file and ensure the key is correctly set."
        )

# Run validation on import so the app fails fast if misconfigured
validate_environment()