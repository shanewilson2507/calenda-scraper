from .ai_agent_interface import AIAgentInterface

from config.ai_agent.groq_agent_config import GROQ_API_ENDPOINT, GROQ_API_KEY, GROQ_MODEL_NAME, GROQ_SEED, GROQ_TEMPERATURE

from openai import OpenAI


class GroqAgent(AIAgentInterface):
    
    def __init__(self, api_key: str = GROQ_API_KEY, seed: str = GROQ_SEED) -> None:

        self.client = OpenAI(
            api_key = api_key, 
            base_url = GROQ_API_ENDPOINT
        )

        self.model = GROQ_MODEL_NAME

        self.temperature = GROQ_TEMPERATURE
        
        self.seed = seed

    
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
        
            messages = messages,

            seed = self.seed
        )

        response_str = response.choices[0].message.content
        
        return response_str