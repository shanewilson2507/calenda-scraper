from abc import ABC, abstractmethod
from typing import List


class ChunkerInterface(ABC):

    @abstractmethod
    def chunk(self, raw_text: str) -> List[str]:
        pass