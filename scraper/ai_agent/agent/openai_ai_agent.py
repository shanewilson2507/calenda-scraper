from .ai_agent_interface import AIAgentInterface

import config.ai_agent.openai_agent_config as config #######

from openai import OpenAI

class OpenaiAgent(AIAgentInterface):
    
    def __init__(self, api_key: str = config.OPENAI_IMAGE_API_KEY, seed: int = config.OPENAI_SEED) -> None:

        self.client = OpenAI(
            api_key = api_key, 
        )

        self.model = config.OPENAI_MODEL_NAME

        self.temperature = config.OPENAI_TEMPERATURE
        
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