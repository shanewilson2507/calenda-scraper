from .ai_agent_interface import AIAgentInterface

import config.ai_agent.gemini_image_agent_config as config

import google.generativeai as genai


class GeminiImageAgent(AIAgentInterface):

    def __init__(self, api_key: str = config.GEMINI_API_KEY) -> None:

        genai.configure(api_key = api_key)

        self.model = config.GEMINI_MODEL_NAME

        self.temperature = config.GEMINI_TEMPERATURE

        self.model_instance = genai.GenerativeModel(
            model_name = self.model,
            generation_config = genai.types.GenerationConfig(
                temperature = self.temperature,
            )
        )
    
    def ask(self, image_bytes: bytes, system_message: str) -> str:

        messages = [
            {
                "role" : "user",
                "parts" : [
                    system_message,
                    {
                        "mime_type" : "image/png",
                        "data" : image_bytes
                    }
                ]
            },
        ]

        response = self.model_instance.generate_content(contents = messages)

        return response.text
