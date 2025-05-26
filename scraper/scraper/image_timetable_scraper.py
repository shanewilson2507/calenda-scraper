from .timetable_scraper_interface import TimetableScraperInterface
from scraper.fetcher.fetcher_interface import FetcherInterface
from scraper.extractor.extractor_interface import ExtractorInterface
from scraper.cleaner.cleaner_interface import CleanerInterface

from typing import List, Dict
import json
import base64


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
        
        base64_jpeg_image: str = self.fetcher.fetch(url)

        self._save_image(base64_jpeg_image)

        timetable = self.timetable_extractor.extract(base64_jpeg_image)
        
        timetable_json_str = json.dumps(timetable)

        cleaned_timetable_json_str =  self.timetable_json_cleaner.clean(timetable_json_str)

        cleaned_timetable = json.loads(cleaned_timetable_json_str)

        return cleaned_timetable
    
    def _save_image(self, base64_jpeg_image: str) -> None:

        with open("page_screenshot.jpeg", "wb") as file:

            jpeg_bytes = base64.b64decode(base64_jpeg_image)

            file.write(jpeg_bytes)

        