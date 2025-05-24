from .chunker_interface import ChunkerInterface

import config.chunker.html_chunker_config as config

from typing import List


class HTMLChunker(ChunkerInterface):

    def __init__(self, max_chunk_size: int = config.HTML_MAX_CHUNK_SIZE):

        self.max_chunk_size = max_chunk_size

    def chunk(self, raw_html: str) -> List[str]:

        html_chunks = []

        file = open("extracted_html.txt", 'w', encoding='utf-8') ##
        j = 1 ##
        
        for i in range(0, len(raw_html), self.max_chunk_size):
        
            chunk = raw_html[i:i + self.max_chunk_size]
        
            html_chunks.append(chunk)

            file.write('\n'*3 + '#'*25 + f'  CHUNK {j}  ' + '#'*25 + '\n'*3 + chunk ) ##
            j += 1 ##
        
        file.close()
        
        return html_chunks
                