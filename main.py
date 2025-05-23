from scraper.factory.selenium_html_timetable_scraper_factory import SeleniumHTMLTimetableScraperFactory

import json


URL_LIST = [
    "https://brandedweb-next.mindbodyonline.com/components/widgets/schedules/view/76181164bc3/schedule"
]

def main():
    scraper = SeleniumHTMLTimetableScraperFactory.create_timetable_scraper()
    
    output = []

    for url in URL_LIST:
        activities = scraper.scrape_timetable(url)
        output.append({"url" : url, "activities" : activities})

    with open("extracted_activities.json", "w") as file:
        json.dump(output, file, indent=4)
    

if __name__ == "__main__":

    main()
