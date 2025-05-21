from ..ai_agent import *
from ..ai_agent.ai_agent_interface import AIAgentInterface
from ..ai_agent.prompt_executor_interface import PromptExecutorInterface
from ..chunker import *
from ..chunker.chunker_interface import ChunkerInterface
from ..fetcher import *
from ..fetcher.fetcher_interface import FetcherInterface
from ..extractor import *
from ..extractor.extractor_interface import ExtractorInterface
from ..cleaner import *
from ..cleaner.cleaner_interface import CleanerInterface
from ..scraper.html_timetable_scraper import HTMLTimetableScraper
from .timetable_scraper_factory_interface import TimetableScraperFactoryInterface

class DefaultHTMLTimetableScraperFactory(TimetableScraperFactoryInterface):

    @staticmethod
    def _create_fetcher() -> FetcherInterface:

        return HTMLFetcher()
    
    @staticmethod
    def _create_html_cleaner() -> CleanerInterface:

        return HTMLCleaner()
    
    @staticmethod
    def _create_chunker() -> ChunkerInterface:
        
        return HTMLChunker()
    
    @staticmethod
    def _create_ai_agent() -> AIAgentInterface:

        return GroqAgent()
    
    @staticmethod
    def _create_prompt_executor() -> PromptExecutorInterface:
        
        return PromptExecutor(ai_agent = DefaultHTMLTimetableScraperFactory._create_ai_agent())
    
    @staticmethod
    def _create_json_extractor() -> ExtractorInterface:

        return RobustJsonExtractor()

    @staticmethod
    def _create_timetable_extractor() -> ExtractorInterface:

        return TimetableExtractor(
            executor = DefaultHTMLTimetableScraperFactory._create_prompt_executor(),
            json_extractor = DefaultHTMLTimetableScraperFactory._create_json_extractor()
            )

    @staticmethod
    def _create_timetable_json_cleaner() -> CleanerInterface:

        return TimetableJsonCleaner()
    
    @staticmethod
    def create_timetable_scraper():
        
        return HTMLTimetableScraper(
            fetcher = DefaultHTMLTimetableScraperFactory._create_fetcher(),
            cleaner = DefaultHTMLTimetableScraperFactory._create_html_cleaner(),
            chunker = DefaultHTMLTimetableScraperFactory._create_chunker(),
            timetable_extractor = DefaultHTMLTimetableScraperFactory._create_timetable_extractor(),
            timetable_json_cleaner = DefaultHTMLTimetableScraperFactory._create_timetable_json_cleaner()
            )
    


