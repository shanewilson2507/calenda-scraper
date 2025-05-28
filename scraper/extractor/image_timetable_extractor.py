from .extractor_interface import ExtractorInterface

from scraper.ai_agent.prompt_executor.prompt_executor_interface import PromptExecutorInterface
import config.extractor.image_timetable_extractor_config as config

from typing import List, Dict

class ImageTimetableExtractor(ExtractorInterface):

    def __init__(self, executor: PromptExecutorInterface, json_extractor: ExtractorInterface) -> None:
        
        self.executor = executor

        self.json_extractor = json_extractor
        
        self.system_message = config.TIMETABLE_EXTRACTOR_SYSTEM_MESSAGE

    def extract(self, base64_image_url: str) -> List[Dict[str, str]]:

        response = self.executor.execute(base64_image_url, self.system_message)

        print(response)

        timetable_content_json = self.json_extractor.extract(response)

        return timetable_content_json

