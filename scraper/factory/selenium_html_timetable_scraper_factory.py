from scraper.ai_agent import GroqAgent, PromptExecutor
from scraper.ai_agent.agent.ai_agent_interface import AIAgentInterface
from scraper.ai_agent.prompt_executor.prompt_executor_interface import PromptExecutorInterface
from scraper.chunker import HTMLChunker
from scraper.chunker.chunker_interface import ChunkerInterface
from scraper.fetcher import SeleniumHTMLFetcher
from scraper.fetcher.fetcher_interface import FetcherInterface
from scraper.extractor import HTMLTimetableExtractor, RobustJsonExtractor
from scraper.extractor.extractor_interface import ExtractorInterface
from scraper.cleaner import HTMLCleaner, TimetableJsonCleaner
from scraper.cleaner.cleaner_interface import CleanerInterface
from scraper.scraper.html_timetable_scraper import HTMLTimetableScraper
from .timetable_scraper_factory_interface import TimetableScraperFactoryInterface

class SeleniumHTMLTimetableScraperFactory(TimetableScraperFactoryInterface):

    @staticmethod
    def _create_fetcher() -> FetcherInterface:

        return SeleniumHTMLFetcher()
    
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
        
        return PromptExecutor(ai_agent = SeleniumHTMLTimetableScraperFactory._create_ai_agent())
    
    @staticmethod
    def _create_json_extractor() -> ExtractorInterface:

        return RobustJsonExtractor()

    @staticmethod
    def _create_timetable_extractor() -> ExtractorInterface:

        return HTMLTimetableExtractor(
            executor = SeleniumHTMLTimetableScraperFactory._create_prompt_executor(),
            json_extractor = SeleniumHTMLTimetableScraperFactory._create_json_extractor()
            )

    @staticmethod
    def _create_timetable_json_cleaner() -> CleanerInterface:

        return TimetableJsonCleaner()
    
    @staticmethod
    def create_timetable_scraper():
        
        return HTMLTimetableScraper(
            fetcher = SeleniumHTMLTimetableScraperFactory._create_fetcher(),
            cleaner = SeleniumHTMLTimetableScraperFactory._create_html_cleaner(),
            chunker = SeleniumHTMLTimetableScraperFactory._create_chunker(),
            timetable_extractor = SeleniumHTMLTimetableScraperFactory._create_timetable_extractor(),
            timetable_json_cleaner = SeleniumHTMLTimetableScraperFactory._create_timetable_json_cleaner()
            )
    


