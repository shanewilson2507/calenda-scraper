from .ai_agent_interface import AIAgentInterface

import config.ai_agent.gemini_agent_config as config

import google.generativeai as genai


class GeminiAgent(AIAgentInterface):

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
    
    def ask(self, user_message:str, system_message: str) -> str:

        message = f"SYSTEM MESSAGE: \n\n{system_message}\n\n USER MESSAGE: \n\n{user_message}"

        messages = [
            {
                "role" : "user",
                "parts" : [message]
            },
        ]

        response = self.model_instance.generate_content(contents = messages)

        return response.text
