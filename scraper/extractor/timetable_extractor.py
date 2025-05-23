from .extractor_interface import ExtractorInterface

from scraper.ai_agent.prompt_executor_interface import PromptExecutorInterface
from config.extractor.timetable_extractor_config import *

from typing import List, Dict

class TimetableExtractor(ExtractorInterface):

    def __init__(self, executor: PromptExecutorInterface, json_extractor: ExtractorInterface) -> None:
        
        self.executor = executor

        self.json_extractor = json_extractor
        
        self.system_message = TIMETABLE_EXTRACTOR_SYSTEM_MESSAGE

        self.user_message_template = TIMETABLE_EXTRACTOR_USER_MESSAGE_TEMPLATE

    def extract(self, raw_html: str) -> List[Dict[str, str]]:

        user_message = self.user_message_template + raw_html

        response = self.executor.execute(user_message = user_message, system_message = self.system_message)

        print(response)

        timetable_content_json = self.json_extractor.extract(response)

        return timetable_content_json

