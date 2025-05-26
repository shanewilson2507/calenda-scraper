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


class ImageFetcher(FetcherInterface):

    service: Service = Service(GeckoDriverManager().install())

    def __init__(self) -> None:

        self.options: Options = Options()

        self.options.add_argument("--headless")

        self.driver: WebDriver = webdriver.Firefox(service = ImageFetcher.service, options = self.options)

    def fetch(self, url: str) -> str:

        self.driver.get(url)

        WebDriverWait(self.driver, 15).until(
            lambda d: d.execute_script('return document.readyState') == 'complete'
        )

        time.sleep(3)

        image = self.driver.get_full_page_screenshot_as_base64()

        base64_jpeg_image = self._convert_to_jpeg(image)

        return base64_jpeg_image
    
    def _convert_to_jpeg(self, base64_image: str) -> str:

        image_bytes = base64.b64decode(base64_image)

        img = Image.open(BytesIO(image_bytes))

        img = img.convert('RGB')

        buffer = BytesIO()

        img.save(buffer, format='JPEG')

        jpeg_bytes = buffer.getvalue()

        base64_jpeg_image = base64.b64encode(jpeg_bytes).decode("utf-8")

        return base64_jpeg_image

    def __enter__(self):

        return self

    def __exit__(self, exc_type, exc_value, traceback):

        self.driver.quit()

    def __del__(self):

        self.driver.quit()

