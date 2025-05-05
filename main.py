from scraper.timetable_scraper import TimetableScraper
import json


URL_LIST = [
    "https://www.thepetiteperformers.com/acton",
    "https://www.thepetiteperformers.com/putney",
    "https://www.thepetiteperformers.com/Notting-Hill",
    "https://www.thepetiteperformers.com/queens-park"
]

def main():
    scraper = TimetableScraper()
    
    output = []

    for url in URL_LIST:
        activities = scraper.scrape(url)
        output.append({"url" : url, "activities" : activities})

    with open("extracted_activities.json", "w") as file:
        json.dump(output, file, indent=4)
    

if __name__ == "__main__":

    main()
