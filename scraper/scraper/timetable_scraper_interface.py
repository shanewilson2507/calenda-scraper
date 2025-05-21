from abc import ABC, abstractmethod
from typing import Dict, List

class TimetableScraperInterface(ABC):

    @abstractmethod
    def scrape_timetable(self, url: str) -> List[Dict[str,str]]:
        pass