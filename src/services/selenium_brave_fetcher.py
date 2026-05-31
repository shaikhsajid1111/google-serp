from seleniumbase import SB
from src.intrefaces.fetcher_html import IHtmlFetcher
from config.settings import PAGE_LOAD_TIMEOUT, SEARCH_BAR_HTML_TAG_NAME
from utils.uri_utils import UriUtils
from utils.force_close_utils import ForceProcessCloseUtils
from src.intrefaces.selenium_browser_configs import SelenmiumBrowserConfig

class SeleniumBaseFetcher(IHtmlFetcher):

    def fetch_serp_html(
        self,
        query: str,
        browser_name: str,
        selenium_browser_config: SelenmiumBrowserConfig,
    ) -> str:

        source_html = ""
        encoded_url = UriUtils.build_query_url(query)

        pids_before = \
            ForceProcessCloseUtils.extract_processes_pids(browser_name.lower())
            
        try:
            with SB(
                browser=browser_name,
                uc=selenium_browser_config.uc,
                headless=False,
                xvfb=False,
            ) as sb:

                sb.open(encoded_url)

                if sb.is_text_visible("checking your browser", "body"):
                    sb.sleep(4)

                sb.wait_for_element(SEARCH_BAR_HTML_TAG_NAME, 
                                    timeout=PAGE_LOAD_TIMEOUT)
                source_html = sb.get_page_source()
        except Exception as ex:
            print(f"Error while fetching page: {ex}")
            return ""

        finally:
            sb.sleep(
                0.5
            )  # Give the context manager a split second to release files
            pids_after = ForceProcessCloseUtils.extract_processes_pids(browser_name.lower())
            # Isolate the exact orphan child processes spawned by our script
            spawned_pids = pids_after - pids_before
            ForceProcessCloseUtils.force_close_processes(spawned_pids)
                

        return source_html
