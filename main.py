from scraper.factory.default_html_timetable_scraper_factory import DefaultHTMLTimetableScraperFactory

import json


URL_LIST = [
    "https://www.thepetiteperformers.com/acton"
]

def main():
    scraper = DefaultHTMLTimetableScraperFactory.create_timetable_scraper()
    
    output = []

    for url in URL_LIST:
        activities = scraper.scrape_timetable(url)
        output.append({"url" : url, "activities" : activities})

    with open("extracted_activities.json", "w") as file:
        json.dump(output, file, indent=4)
    

if __name__ == "__main__":

    main()
