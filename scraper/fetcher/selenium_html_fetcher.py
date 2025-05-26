from .fetcher_interface import FetcherInterface

import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait


class SeleniumHTMLFetcher(FetcherInterface):

    service: Service = Service(ChromeDriverManager().install())

    def __init__(self):

        self.options: Options = Options()

        self.options.add_argument("--headless")

        self.driver: WebDriver = webdriver.Chrome(service = SeleniumHTMLFetcher.service, options = self.options)

    def fetch(self, url: str) -> str:

        self.driver.get(url)

        time.sleep(10)

        raw_html: str = self.driver.page_source

        return raw_html
    
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.driver.quit()
    
    def __del__(self):
        self.driver.quit()
