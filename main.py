import sys
from src.factories.fetcher_factory import Fetcherfactory
from src.services.parser_html import GoogleSerpParser
from src.orchestrator import GoogleScraperOrchestrator
from src.intrefaces.selenium_browser_configs import SeleniumBrowserConfig
from src.services.json_exporter import JsonExporter


def main():
    browser_input = input("Select Browser (chrome/brave): ")
    query = input("Enter search query: ")
    config: SeleniumBrowserConfig = SeleniumBrowserConfig(
        uc=True, browser_path="/usr/bin/google-chrome", headless=False, proxy=None
    )
    try:
        fetcher = Fetcherfactory.create_fetcher(browser_input)
        parser = GoogleSerpParser()
        data_exporter = JsonExporter()

        scraper = GoogleScraperOrchestrator(fetcher, parser, data_exporter)
        data = scraper.scrape(query, 10, browser_input, config)
        print(data)

    except Exception as ex:
        print(f"Error running scraper: {ex}", file=sys.stderr)


if __name__ == "__main__":
    main()
