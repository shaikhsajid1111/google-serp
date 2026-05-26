from src.intrefaces.fetcher_html import IHtmlFetcher
from src.services.selenium_brave_fetcher import SeleniumBaseFetcher
from src.intrefaces.selenium_browser_configs import SelenmiumBrowserConfig


class Fetcherfactory:
    @staticmethod
    def create_fetcher(browser_type: str) -> IHtmlFetcher:
        supported = ["chrome", "brave"]
        normalized = browser_type.lower()
        if normalized in supported:
            return SeleniumBaseFetcher()
        raise ValueError(f"Browser : '{browser_type}' not supported")
