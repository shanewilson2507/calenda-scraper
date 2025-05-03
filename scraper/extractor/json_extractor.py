from .extractor_interface import ExtractorInterface

from typing import List, Dict
import json


class JsonExtractor(ExtractorInterface):

    def extract(self, json_str: str) -> List[Dict[str, str]]:
        
        try:

            print(json_str)
        
            return json.loads(json_str)
        
        except:
        
            return []
