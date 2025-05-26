from scraper.ai_agent import OpenaiImageAgent, PromptExecutor
from scraper.ai_agent.agent.ai_agent_interface import AIAgentInterface
from scraper.ai_agent.prompt_executor.prompt_executor_interface import PromptExecutorInterface
from scraper.fetcher import ImageFetcher
from scraper.fetcher.fetcher_interface import FetcherInterface
from scraper.extractor import ImageTimetableExtractor, RobustJsonExtractor
from scraper.extractor.extractor_interface import ExtractorInterface
from scraper.cleaner import TimetableJsonCleaner
from scraper.cleaner.cleaner_interface import CleanerInterface
from scraper.scraper.image_timetable_scraper import ImageTimetableScraper
from .timetable_scraper_factory_interface import TimetableScraperFactoryInterface

class DefaultImageTimetableScraperFactory(TimetableScraperFactoryInterface):

    @staticmethod
    def _create_fetcher() -> FetcherInterface:

        return ImageFetcher()
    
    @staticmethod
    def _create_ai_agent() -> AIAgentInterface:

        return OpenaiImageAgent()
    
    @staticmethod
    def _create_prompt_executor() -> PromptExecutorInterface:
        
        return PromptExecutor(ai_agent = DefaultImageTimetableScraperFactory._create_ai_agent())
    
    @staticmethod
    def _create_json_extractor() -> ExtractorInterface:

        return RobustJsonExtractor()

    @staticmethod
    def _create_timetable_extractor() -> ExtractorInterface:

        return ImageTimetableExtractor(
            executor = DefaultImageTimetableScraperFactory._create_prompt_executor(),
            json_extractor = DefaultImageTimetableScraperFactory._create_json_extractor()
            )

    @staticmethod
    def _create_timetable_json_cleaner() -> CleanerInterface:

        return TimetableJsonCleaner()
    
    @staticmethod
    def create_timetable_scraper():
        
        return ImageTimetableScraper(
            fetcher = DefaultImageTimetableScraperFactory._create_fetcher(),
            timetable_extractor = DefaultImageTimetableScraperFactory._create_timetable_extractor(),
            timetable_json_cleaner = DefaultImageTimetableScraperFactory._create_timetable_json_cleaner()
            )
    


