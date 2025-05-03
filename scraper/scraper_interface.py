from abc import ABC, abstractmethod
from typing import Dict, List

class ScraperInterface(ABC):

    @abstractmethod
    def scrape(self, url: str) -> List[Dict[str,str]]:
        pass