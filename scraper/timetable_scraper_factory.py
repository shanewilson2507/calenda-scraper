from .ai_agent import *
from .ai_agent.ai_agent_interface import AIAgentInterface
from .ai_agent.prompt_executor_interface import PromptExecutorInterface
from .chunker import *
from .chunker.chunker_interface import ChunkerInterface
from .fetcher import *
from .fetcher.fetcher_interface import FetcherInterface
from .extractor import *
from .extractor.extractor_interface import ExtractorInterface
from .cleaner import *
from .cleaner.cleaner_interface import CleanerInterface


class TimetableScraperFactory:

    @staticmethod
    def create_fetcher() -> FetcherInterface:

        return HTMLFetcher()
    
    @staticmethod
    def create_html_cleaner() -> CleanerInterface:

        return HTMLCleaner()
    
    @staticmethod
    def create_chunker() -> ChunkerInterface:
        
        return HTMLChunker()
    
    @staticmethod
    def create_ai_agent() -> AIAgentInterface:

        return GroqAgent()
    
    @staticmethod
    def create_prompt_executor() -> PromptExecutorInterface:
        
        return PromptExecutor(ai_agent = TimetableScraperFactory.create_ai_agent())
    
    @staticmethod
    def create_json_extractor() -> ExtractorInterface:

        return RobustJsonExtractor()

    @staticmethod
    def create_timetable_extractor() -> ExtractorInterface:

        return TimetableExtractor(
            executor = TimetableScraperFactory.create_prompt_executor(),
            json_extractor = TimetableScraperFactory.create_json_extractor()
            )

    @staticmethod
    def create_timetable_json_cleaner() -> CleanerInterface:

        return TimetableJsonCleaner()
    


