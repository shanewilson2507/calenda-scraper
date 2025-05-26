import os
from dotenv import load_dotenv


load_dotenv()

OPENAI_IMAGE_API_KEY = os.getenv("OPENAI_IMAGE_API_KEY")

OPENAI_MODEL_NAME = "gpt-4o"

OPENAI_TEMPERATURE = 0.1

OPENAI_SEED = 1234