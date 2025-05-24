from .cleaner_interface import CleanerInterface

import config.cleaner.html_cleaner_config as config

from bs4 import BeautifulSoup
import htmlmin


class HTMLCleaner(CleanerInterface):

    def clean(self, raw_html: str) -> str:
        
        soup = BeautifulSoup(raw_html, "html.parser")

        body_soup = BeautifulSoup(str(soup.body), "html.parser")

        for tag in body_soup(config.REMOVABLE_TAGS_LIST):
            
            tag.decompose()         

        clean_html = htmlmin.minify(
            str(body_soup),  
            remove_comments = config.REMOVE_COMMENTS, 
            reduce_boolean_attributes = config.REDUCE_BOOLEAN_ATTRIBUTES,
            reduce_empty_attributes = config.REDUCE_EMPTY_ATTRIBUTES,
            remove_empty_space = config.REMOVE_EMPTY_SPACE
        )

        pretty_html = BeautifulSoup(clean_html, "html.parser").prettify()

        return pretty_html