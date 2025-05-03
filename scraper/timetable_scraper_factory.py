from .ai_agent import *
from .ai_agent.ai_agent_interface import AIAgentInterface
from .ai_agent.prompt_executor_interface import PromptExecutorInterface
from .chunker import *
from .chunker.chunker_interface import ChunkerInterface
from .fetcher import *
from .fetcher.fetcher_interface import FetcherInterface
from .extractor import *
from .extractor.extractor_interface import ExtractorInterface


class TimetableScraperFactory:

    @staticmethod
    def create_fetcher() -> FetcherInterface:

        return HTMLFetcher()
    
    @staticmethod
    def create_chunker() -> ChunkerInterface:
        
        return HTMLChunker()
    
    @staticmethod
    def create_ai_agent() -> AIAgentInterface:

        return GroqAgent()
    
    @staticmethod
    def create_prompt_exexutor() -> PromptExecutorInterface:
        
        return PromptExecutor(ai_agent = TimetableScraperFactory.create_ai_agent())
    
    @staticmethod
    def create_json_extractor() -> ExtractorInterface:

        return JsonExtractor()

    @staticmethod
    def create_timetable_extractor() -> ExtractorInterface:

        return TimetableExtractor(
            executor = TimetableScraperFactory.create_prompt_exexutor(),
            json_extractor = TimetableScraperFactory.create_json_extractor()
            )
    


