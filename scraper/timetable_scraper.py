from .scraper_interface import ScraperInterface
from .fetcher.fetcher_interface import FetcherInterface
from .chunker.chunker_interface import ChunkerInterface
from .extractor.extractor_interface import ExtractorInterface
from .timetable_scraper_factory import TimetableScraperFactory


from typing import List, Dict


class TimetableScraper(ScraperInterface):

    def __init__(
            self,
            fetcher: FetcherInterface = TimetableScraperFactory.create_fetcher(),
            chunker: ChunkerInterface = TimetableScraperFactory.create_chunker(),
            timetable_extractor: ExtractorInterface = TimetableScraperFactory.create_timetable_extractor()
            ):
        
        self.fetcher = fetcher
        
        self.chunker = chunker
        
        self.timetable_extractor = timetable_extractor

    def scrape(self, url: str) -> List[Dict[str,str]]:

        timetable = []
        
        raw_html: str = self.fetcher.fetch(url)

        for html_chunk in self.chunker.chunk(raw_html):

            timetable += self.timetable_extractor.extract(html_chunk)
        
        return timetable





