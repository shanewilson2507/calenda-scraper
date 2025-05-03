from abc import ABC, abstractmethod


class FetcherInterface(ABC):
    
    @abstractmethod
    def fetch(self, url: str) -> str:
        pass

