from .prompt_executor_interface import PromptExecutorInterface
from ..agent.ai_agent_interface import AIAgentInterface

from exceptions.max_retries_exceeded_error import MaxRetriesExceededError
import config.ai_agent.prompt_executor_config as config

from openai import RateLimitError

import time


class PromptExecutor(PromptExecutorInterface):

    def __init__(
            self, 
            ai_agent: AIAgentInterface, 
            max_retries: int = config.PROMPT_MAX_RETRIES, 
            backoff_factor: float = config.PROMPT_BACKOFF_FACTOR
            ) -> None:
        
        self.ai_agent = ai_agent
        
        self.max_retries = max_retries
        
        self.backoff_factor = backoff_factor

    def execute(self, user_message: str, system_message: str) -> str:
        
        for attempt in range(1, self.max_retries + 1):
        
            try:
        
                return self.ai_agent.ask(user_message, system_message)
        
            except RateLimitError:
        
                if attempt == self.max_retries:
        
                    raise MaxRetriesExceededError("Maximum retries exceeded")
        
                wait_time = self.backoff_factor ** (attempt - 1)
        
                time.sleep(wait_time)