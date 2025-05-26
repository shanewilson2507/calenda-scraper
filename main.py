from scraper.factory.default_html_timetable_scraper_factory import DefaultHTMLTimetableScraperFactory
from scraper.factory.default_image_timetable_scraper_factory import DefaultImageTimetableScraperFactory

import json


URL_LIST = [
    "https://salsa4fun.co.uk/class-schedule"
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

    from scraper.fetcher import ImageFetcher
    import base64

    image = ImageFetcher().fetch("https://salsa4fun.co.uk/class-schedule")

    with open("page_screenshot.jpeg", "wb") as file:
        
        image_bytes = base64.b64decode(image)

        file.write(image_bytes)
    
if __name__ == "__main__":

    main()
