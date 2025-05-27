from .cleaner_interface import CleanerInterface

from typing import List, Dict

import json

class TimetableJsonCleaner(CleanerInterface):

    def clean(self, json_str: str) -> str:

        timetable: List[Dict[str, str]] = json.loads(json_str)

        clean_timetable = []

        for activity in timetable:

            if (
                verify_field_exists('activity_name', activity)
                and verify_field_exists('start_time', activity)
                ):

                clean_timetable.append(activity)

        clean_timetable = remove_empty_fields(clean_timetable)

        return json.dumps(clean_timetable)

def verify_field_exists(field: str, data: Dict[str,str]) -> bool:
    
    return (field in data) and (field)

def remove_empty_fields(data: List[Dict[str, str]]) -> List[Dict[str, str]]:
    
    return [{k: v for k, v in item.items() if v.strip()} for item in data]
