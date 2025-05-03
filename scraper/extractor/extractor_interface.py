from abc import ABC, abstractmethod
from typing import List, Dict

class ExtractorInterface(ABC):

    @abstractmethod
    def extract(self, raw_text: str) -> List[Dict[str,str]]:
        pass