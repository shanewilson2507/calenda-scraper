from abc import ABC, abstractmethod


class PromptExecutorInterface(ABC):

    @abstractmethod
    def execute(self, user_message: str, system_message: str) -> str:
        pass