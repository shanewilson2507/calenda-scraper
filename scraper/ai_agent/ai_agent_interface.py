from abc import ABC, abstractmethod


class AIAgentInterface(ABC):
    
    @abstractmethod
    def ask(self, user_message: str, system_message: str) -> str:
        pass
