from .cleaner_interface import CleanerInterface

from config.cleaner.html_cleaner_config import *

from bs4 import BeautifulSoup
import htmlmin


class HTMLCleaner(CleanerInterface):

    def clean(self, raw_html: str) -> str:
        
        soup = BeautifulSoup(raw_html, "html.parser")

        body_soup = BeautifulSoup(str(soup.body), "html.parser")

        for tag in body_soup(REMOVABLE_TAGS_LIST):
            
            tag.decompose()         

        clean_html = htmlmin.minify(
            str(body_soup),  
            remove_comments=REMOVE_COMMENTS, 
            reduce_boolean_attributes=REDUCE_BOOLEAN_ATTRIBUTES,
            reduce_empty_attributes=REDUCE_EMPTY_ATTRIBUTES,
            remove_empty_space=REMOVE_EMPTY_SPACE
        )

        pretty_html = BeautifulSoup(clean_html, "html.parser").prettify()

        return pretty_html