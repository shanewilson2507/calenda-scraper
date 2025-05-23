from .fetcher_interface import FetcherInterface

import requests

class HTMLFetcher(FetcherInterface):

    def fetch(self, url: str) -> str:

        headers = {
            "Accept" : "text/html",
            "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
        }

        response = requests.get(url=url, headers=headers)

        response.raise_for_status()

        raw_html = response.text

        return raw_html
    
