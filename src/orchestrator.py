from typing import List
from src.intrefaces.fetcher_html import IHtmlFetcher
from src.intrefaces.parser_html import IhtmlParser
from src.models.search_result import SearchResult
from src.intrefaces.selenium_browser_configs import SeleniumBrowserConfig
from src.intrefaces.exporter import IDataExporter
from src.intrefaces.parser_confg import ParserConfig


class GoogleScraperOrchestrator:
    def __init__(
        self, fetcher: IHtmlFetcher, parser: IhtmlParser, data_exporter: IDataExporter
    ):
        self._fetcher = fetcher
        self._parser = parser
        self._data_exporter = data_exporter

    def scrape(
        self,
        query: str,
        max_results: int,
        browser_name: str,
        selenium_browser_config: SeleniumBrowserConfig,
    ) -> List[SearchResult]:
        raw_html = self._fetcher.fetch_serp_html(
            query, browser_name, selenium_browser_config
        )
        parser_config = ParserConfig(raw_html_content=raw_html, max_result=max_results)
        parsed_data = self._parser.parse(parser_config)
        return self._data_exporter.export(parsed_data)
