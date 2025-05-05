import os
from dotenv import load_dotenv


load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

GROQ_MODEL_NAME = "llama3-8b-8192"

GROQ_API_ENDPOINT = "https://api.groq.com/openai/v1"

GROQ_TEMPERATURE = 0.1