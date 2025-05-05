from .scraper_interface import ScraperInterface
from .fetcher.fetcher_interface import FetcherInterface
from .chunker.chunker_interface import ChunkerInterface
from .extractor.extractor_interface import ExtractorInterface
from .cleaner.cleaner_interface import CleanerInterface
from .timetable_scraper_factory import TimetableScraperFactory


from typing import List, Dict
import json


class TimetableScraper(ScraperInterface):

    def __init__(
            self,
            fetcher: FetcherInterface = TimetableScraperFactory.create_fetcher(),
            cleaner: CleanerInterface = TimetableScraperFactory.create_html_cleaner(),
            chunker: ChunkerInterface = TimetableScraperFactory.create_chunker(),
            timetable_extractor: ExtractorInterface = TimetableScraperFactory.create_timetable_extractor(),
            timetable_json_cleaner: CleanerInterface = TimetableScraperFactory.create_timetable_json_cleaner()
            ):
        
        self.fetcher = fetcher

        self.cleaner = cleaner
        
        self.chunker = chunker
        
        self.timetable_extractor = timetable_extractor

        self.timetable_json_cleaner = timetable_json_cleaner

    def scrape(self, url: str) -> List[Dict[str,str]]:

        timetable = []
        
        raw_html: str = self.fetcher.fetch(url)

        clean_html: str = self.cleaner.clean(raw_html)

        for html_chunk in self.chunker.chunk(clean_html):

            timetable += self.timetable_extractor.extract(html_chunk)
        
        timetable_json_str = json.dumps(timetable)

        cleaned_timetable_json_str =  self.timetable_json_cleaner.clean(timetable_json_str)

        cleaned_timetable = json.loads(cleaned_timetable_json_str)

        return cleaned_timetable





