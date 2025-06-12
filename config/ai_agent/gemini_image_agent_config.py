import os
from dotenv import load_dotenv


load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

GEMINI_MODEL_NAME = "gemini-2.0-flash"

GEMINI_TEMPERATURE = 0.1