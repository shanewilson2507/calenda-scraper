
ACTIVITY_TYPES = (
    "[Ballet, Jazz, Musical Theatre, Lyrical, Gymnastics, Contemporary, Drama, Tap, "
    "Acro, HipHop, Street Dance, Competition, Boys, Ballroom, Disco]"
)

FIELDS_TO_EXTRACT = (
    "\n"
    "Here is the list of data fields along with their explanations: \n\n"
    "- activity_name: The name or title of the activity/lesson.\n"
    "- format: The format of the activity. You MUST match to one of the following: [Class, Camp, Event].\n"
   f"- activity_type: The specific type of activity. TRY to match to one of the following: {ACTIVITY_TYPES}. If NO MATCH is found, you MUST use 'Other'.\n"
    "- start_time: The starting time of the activity in MILITARY TIME format HH:MM:SS.\n"
    "- end_time: The ending time of the activity in MILITARY TIME format HH:MM:SS.\n"
    "- age_range: The target age range for the activity. This MUST be a valid number range of the form A-B. If only one number is shown, list the number range as: from x to x+2(e.g. if 4, or 4+ is shown; list as 4–6).\n"
    "- location: The name of the location the activity is taking place. For example, the name of the school or general location. Note this is NOT the address.\n"
    "- address: The address where the activity is taking place. You MUST include: street address, city, postcode, country. Optionally, include the specific location/building name.\n"
    "- day_of_week: The specific day of the week the activity is scheduled (e.g., 'Monday'). Note this is NOT applicable if the format field is 'Camp'.\n"
    "- term: The term the activity belongs to. You MUST match to one of the following: [Fall, Spring, Summer, Summer Holidays]. Please use the following mappings if required: Fall = Autumn = (Sept-Dec); Spring = Winter = (Jan-April); Summer = (April-July); Summer Holidays = (July-Sept).\n"
    "- term_start: The specific date the term starts. You MUST use the following format: DD.MM.YYYY.\n"
    "- term_end: The specific date the term ends. You MUST use the following format: DD.MM.YYYY.\n"
    "- break_start: The start date of any term breaks. You MUST use the following format: DD.MM.YYYY.\n"
    "- break_end: The end date of any term breaks. You MUST use the following format: DD.MM.YYYY.\n"
    "- bank_holidays: A list of dates of all bank holidays that occur during the activity provider's term time. You MUST use the following format: comma seperated list of DD.MM.YYYY. DO NOT include brackets.\n"
    "- parent_watching_days: A list of parent watching dates. You MUST use the following format: comma seperated list of DD.MM.YYYY. DO NOT include brackets.\n"
    "- application_open_day: The specific date where applications for the activity open. You MUST use the following format: DD.MM.YYYY.\n"
    "- application_open_day: The specific date where applications for the activity close. You MUST use the following format: DD.MM.YYYY.\n"
    
    "\n Note that if a field cannot be extracted you MUST fill it with ''. Include ALL activity objects - even if some are very similar.\n"
)