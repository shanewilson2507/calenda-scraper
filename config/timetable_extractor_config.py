TIMETABLE_EXTRACTOR_SYSTEM_MESSAGE = (
            "You are a strict HTML parser that extracts timetable lessons into JSON format. "
            "ONLY extract data that is explicitly present. "
            "Respond ONLY with a valid JSON array — no explanations, markdown, or extra text. "
            "If a field cannot be filled from the HTML, use an empty string ''."
            "You may infer some fields provided there is enough information."
            "If no lessons can be extracted, respond with an empty JSON array."
        )


TIMETABLE_EXTRACTOR_USER_MESSAGE_TEMPLATE = (
            "Please extract all lessons from the following HTML content. "
            "Each lesson should include:\n\n"
            "-name: <name/title of class>\n"
            "-format: <format of the lesson, eg. group class,camp...>\n"
            "-duration: <lesson duration time>\n"
            "-start_time: <lesson start time>\n"
            "-end_time: <lesson end time>\n"
            "-term: <the term the class is for eg./ Summer>\n"
            "-age_range: <age range the class is aimed at>\n"
            "-recurrence: <class recurrence eg . daily, weekly>\n"
            "-day_of_week: <Day of the week the class takes place>\n"
            "-date_range: <date range of the class>\n"
            "-address: <exact FULL ADDRESS where the lesson takes place. Ensure it is an actual address>\n"
            "-venue_name: <name of the venue where the class takes place. Just the name of the venue - no other address related info>\n"
            "-location: <the general area the class is eg./ town, city or area>\n" 
            "\n\n"
            "Here is the HTML:\n\n"
        )
