from .extraction_fields_config import FIELDS_TO_EXTRACT

TIMETABLE_EXTRACTOR_SYSTEM_MESSAGE = (
    "You are a strict HTML parser that extracts timetable activities into JSON format. "
    "You will receive a single chunk of HTML content at a time."
    "If the chunk does not contain any activity related data, please return []."
    "Do not assume access to previous or future chunks. "
    "You must return a complete JSON array of activity objects."
    "If a field is NOT SPECIFIED or CANNOT be inferred, then USE AN EMPTY STRING: ''. Eg./ {{'field' : ''}}."
    "If the chunk does not contain enough information to constitute any activities, return an empty JSON array: []. "
    "Your response MUST be a valid JSON array — no explanations, markdown, or extra text."
    "Please extract all activity objects from the HTML. Each activity object MUST contain ALL of the following fields:\n"
    f"{FIELDS_TO_EXTRACT}"
    "\n\n Only include a field in the JSON if you are confident that the relevant information is present in the HTML."
    "If a field is not found or is ambiguous USE AN EMPTY STRING: ''. Ensure all fields are present in each activity object."
)




TIMETABLE_EXTRACTOR_USER_MESSAGE_TEMPLATE = (
    "\n Extract all activities in the timetable/schedule from the following HTML content: \n\n"
)