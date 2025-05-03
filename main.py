from scraper.timetable_scraper import TimetableScraper


def main():

    scraper = TimetableScraper()

    timetable = scraper.scrape("https://www.thepetiteperformers.com/Notting-Hill")

    import json
    with open(".lessons.json", "w") as file:
        json.dump(timetable, file, indent = 4)

if __name__ == "__main__":

    main()