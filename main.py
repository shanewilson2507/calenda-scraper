from scraper.factory.default_html_timetable_scraper_factory import DefaultHTMLTimetableScraperFactory
from scraper.factory.default_image_timetable_scraper_factory import DefaultImageTimetableScraperFactory
from scraper.factory.selenium_html_timetable_scraper_factory import SeleniumHTMLTimetableScraperFactory

import json

"""
import base64
with open("page_screenshot.png", "rb") as file:
    base64_image = base64.b64encode(file.read()).decode("utf-8")
    base64_image_url = f"data:image/png;base64,{base64_image}"
"""

URL_LIST = [
    "https://enodanse.live.baluu.co.uk/timetable"
]

def main():
    scraper = DefaultImageTimetableScraperFactory.create_timetable_scraper()
    
    output = []

    for url in URL_LIST:
        activities = scraper.scrape_timetable(url)
        output.append({"url" : url, "activities" : activities})

    with open("extracted_activities.json", "w") as file:
        json.dump(output, file, indent=4)

def test():
    from scraper.ai_agent import GeminiImageAgent

    agent = GeminiImageAgent()

    with open("page_screenshot.png", 'rb') as file:
        image = file.read()


    print(agent.ask(image, "Extract all timetable data in json format from the image below:" ))
    
if __name__ == "__main__":

    test()
