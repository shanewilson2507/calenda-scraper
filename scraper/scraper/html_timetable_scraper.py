from .timetable_scraper_interface import TimetableScraperInterface
from ..fetcher.fetcher_interface import FetcherInterface
from ..chunker.chunker_interface import ChunkerInterface
from ..extractor.extractor_interface import ExtractorInterface
from ..cleaner.cleaner_interface import CleanerInterface


from typing import List, Dict
import json


class HTMLTimetableScraper(TimetableScraperInterface):

    def __init__(
            self,
            fetcher: FetcherInterface,
            cleaner: CleanerInterface,
            chunker: ChunkerInterface,
            timetable_extractor: ExtractorInterface,
            timetable_json_cleaner: CleanerInterface
            ):
        
        self.fetcher = fetcher

        self.cleaner = cleaner
        
        self.chunker = chunker
        
        self.timetable_extractor = timetable_extractor

        self.timetable_json_cleaner = timetable_json_cleaner

    def scrape_timetable(self, url: str) -> List[Dict[str,str]]:

        timetable = []
        
        raw_html: str = self.fetcher.fetch(url)

        clean_html: str = self.cleaner.clean(raw_html)

        for html_chunk in self.chunker.chunk(clean_html):

            timetable += self.timetable_extractor.extract(html_chunk)
        
        timetable_json_str = json.dumps(timetable)

        cleaned_timetable_json_str =  self.timetable_json_cleaner.clean(timetable_json_str)

        cleaned_timetable = json.loads(cleaned_timetable_json_str)

        return cleaned_timetable





