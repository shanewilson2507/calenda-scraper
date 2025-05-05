from .extractor_interface import ExtractorInterface

from typing import List, Dict

import json


class RobustJsonExtractor(ExtractorInterface):

    def extract(self, raw_text: str) -> List[Dict[str,str]]:

        return extract_json_robustly(raw_text)
        

def extract_json_robustly(raw_str: str) -> List[Dict[str,str]]:
    objects = []
    brace_count = 0
    current_obj = ''
    inside_obj = False

    for char in raw_str:
        if char == '{':
            brace_count += 1
            inside_obj = True
        if inside_obj:
            current_obj += char
        if char == '}':
            brace_count -= 1
            if brace_count == 0:
                try:
                    obj = json.loads(current_obj)
                    objects.append(obj)
                except json.JSONDecodeError:
                    pass  # skip malformed object
                current_obj = ''
                inside_obj = False

    return objects