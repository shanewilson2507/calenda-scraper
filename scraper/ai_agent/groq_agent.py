from .ai_agent_interface import AIAgentInterface

from config.groq_agent_config import *

from openai import OpenAI


class GroqAgent(AIAgentInterface):
    
    def __init__(self, api_key: str = GROQ_API_KEY) -> None:

        self.client = OpenAI(
            api_key = api_key, 
            base_url = GROQ_API_ENDPOINT
        )

        self.model = GROQ_MODEL_NAME

        self.temperature = GROQ_TEMPERATURE

    
    def ask(self, user_message: str, system_message: str) -> str:
        
        messages = [
                {
                    "role" : "system",
                    "content" : system_message
                },
                {
                    "role" : "user",
                    "content" : user_message
                }
        ]

        response = self.client.chat.completions.create(
            
            model = self.model,
        
            temperature = self.temperature,
        
            messages = messages
        )

        response_str = response.choices[0].message.content
        
        return response_str