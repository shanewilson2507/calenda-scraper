from .cleaner_interface import CleanerInterface

from typing import List, Dict

import json

class TimetableJsonCleaner(CleanerInterface):

    def clean(self, json_str: str) -> str:

        timetable: List[Dict[str, str]] = json.loads(json_str)

        clean_timetable = []

        for activity in timetable:

            if activity["activity_name"] != "" and activity["start_time"] != "":

                clean_timetable.append(activity)

        return json.dumps(clean_timetable)
