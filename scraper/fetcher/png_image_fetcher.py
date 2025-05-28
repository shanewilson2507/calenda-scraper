from .fetcher_interface import FetcherInterface

import time

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from PIL import Image
from io import BytesIO
import base64


class PngImageFetcher(FetcherInterface):

    try:

        service: Service = Service(GeckoDriverManager().install())
    
    except:

        service: Service = Service("drivers\\geckodriver.exe")

    def __init__(self) -> None:

        self.options: Options = Options()

        self.options.add_argument("--headless")

        self.driver: WebDriver = webdriver.Firefox(service = PngImageFetcher.service, options = self.options)

    def fetch(self, url: str) -> str:

        self.driver.get(url)

        WebDriverWait(self.driver, 15).until(
            lambda d: d.execute_script('return document.readyState') == 'complete'
        )

        time.sleep(10)

        base64_png_image = self.driver.get_full_page_screenshot_as_base64()

        self._save_image(base64_png_image)

        base64_jpeg_image_url = f"data:image/png;base64,{base64_png_image}"

        return base64_jpeg_image_url

    def _save_image(self, base64_png_image: str) -> None:

        with open("page_screenshot.png", "wb") as file:

            png_bytes = base64.b64decode(base64_png_image)

            file.write(png_bytes)

    def __enter__(self):

        return self

    def __exit__(self, exc_type, exc_value, traceback):

        self.driver.quit()

    def __del__(self):

        self.driver.quit()

