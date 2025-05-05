from scraper.timetable_scraper import TimetableScraper
import json


def main():
    scraper = TimetableScraper()

    timetable = scraper.scrape("https://marblehilldancestudio.co.uk/timetable-12-years/")

    with open("extracted_activities.json", "w") as file:
        json.dump(timetable, file, indent=4)
    

if __name__ == "__main__":

    main()
