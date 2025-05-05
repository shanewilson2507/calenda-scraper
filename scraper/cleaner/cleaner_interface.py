from abc import ABC, abstractmethod


class CleanerInterface(ABC):

    @abstractmethod
    def clean(self, raw_text: str) -> str:
        pass