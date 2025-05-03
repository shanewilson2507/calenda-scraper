from .fetcher_interface import FetcherInterface

import requests


class HTMLFetcher(FetcherInterface):

    def fetch(self, url: str) -> str:

        headers = {
            "Accept" : "text/html"
        }

        response = requests.get(url=url, headers=headers)

        response.raise_for_status()

        raw_html = response.text

        return raw_html
    
