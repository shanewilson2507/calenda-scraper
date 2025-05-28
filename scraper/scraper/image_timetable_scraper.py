from .timetable_scraper_interface import TimetableScraperInterface
from scraper.fetcher.fetcher_interface import FetcherInterface
from scraper.extractor.extractor_interface import ExtractorInterface
from scraper.cleaner.cleaner_interface import CleanerInterface

from typing import List, Dict
import json


class ImageTimetableScraper(TimetableScraperInterface):

    def __init__(
            self,
            fetcher: FetcherInterface,
            timetable_extractor: ExtractorInterface,
            timetable_json_cleaner: CleanerInterface
            ):
        
        self.fetcher = fetcher
        
        self.timetable_extractor = timetable_extractor

        self.timetable_json_cleaner = timetable_json_cleaner

    def scrape_timetable(self, url: str) -> List[Dict[str,str]]:
        
        base64_image_url: str = self.fetcher.fetch(url)

        timetable = self.timetable_extractor.extract(base64_image_url)
        
        timetable_json_str = json.dumps(timetable)

        cleaned_timetable_json_str =  self.timetable_json_cleaner.clean(timetable_json_str)

        cleaned_timetable = json.loads(cleaned_timetable_json_str)

        return cleaned_timetable


        