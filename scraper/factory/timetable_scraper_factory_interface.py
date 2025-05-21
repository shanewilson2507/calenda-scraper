from abc import ABC, abstractmethod

from ..scraper.timetable_scraper_interface import TimetableScraperInterface


class TimetableScraperFactoryInterface(ABC):

    @staticmethod
    @abstractmethod
    def create_timetable_scraper() -> TimetableScraperInterface:
        pass