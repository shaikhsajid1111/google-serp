from bs4 import BeautifulSoup
from typing import List
from src.intrefaces.parser_html import IhtmlParser
from src.models.search_result import SearchResult
from config import settings
from src.intrefaces.parser_confg import ParserConfig
from config.settings import RESULT_HEADLINE_SELECTOR

class GoogleSerpParser(IhtmlParser):

    def parse(self, parser_config: ParserConfig):
        results: List[SearchResult] = []
        soup = BeautifulSoup(parser_config.raw_html_content, "html.parser")
        h3_tags = soup.select(RESULT_HEADLINE_SELECTOR)

        for h3 in h3_tags[: parser_config.max_result]:
            title = h3.get_text(strip=True)
            # Navigate up to find the parent anchor tag
            anchor = h3.find_parent("a")
            href = anchor.get("href") if anchor else None

            if title and href:
                results.append(SearchResult(title=title, url=href))

        return results
