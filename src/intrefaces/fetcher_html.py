from abc import ABC, abstractmethod
from src.intrefaces.selenium_browser_configs import SeleniumBrowserConfig


class IHtmlFetcher(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def fetch_serp_html(
        self,
        query: str,
        browser_name: str,
        selenium_browser_config: SeleniumBrowserConfig,
    ) -> str:
        pass
