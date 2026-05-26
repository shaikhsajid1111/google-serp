from seleniumbase import SB
from src.intrefaces.fetcher_html import IHtmlFetcher
from config.settings import PAGE_LOAD_TIMEOUT
from utils.uri_utils import UriUtils
from time import sleep
from src.intrefaces.selenium_browser_configs import SelenmiumBrowserConfig
import subprocess
import os
import signal


class SeleniumBaseFetcher(IHtmlFetcher):

    def fetch_serp_html(
        self,
        query: str,
        browser_name: str,
        selenium_browser_config: SelenmiumBrowserConfig,
    ) -> str:

        source_html = ""
        encoded_url = UriUtils.build_query_url(query)

        # 1. Take a snapshot of all active Brave PIDs before we launch our session
        pids_before = set()
        if "brave" in browser_name.lower():
            try:
                output = subprocess.check_output(["pgrep", "-f", "brave"])
                pids_before = set(output.decode().strip().split())
            except Exception:
                pass

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

                sb.wait_for_element("#search", timeout=PAGE_LOAD_TIMEOUT)
                source_html = sb.get_page_source()

                # Let the block finish naturally to prevent thread-lock exceptions

        except Exception as ex:
            print(f"Error while fetching page: {ex}")
            return ""

        finally:
            # 2. THE ULTIMATE KERNEL-LEVEL PURGE
            # If Brave is running, we find exactly which processes were created
            # by this specific script execution and kill them directly via OS signals.
            if "brave" in browser_name.lower():
                sb.sleep(
                    0.5
                )  # Give the context manager a split second to release files
                try:
                    # Capture all running brave PIDs now
                    output_after = subprocess.check_output(["pgrep", "-f", "brave"])
                    pids_after = set(output_after.decode().strip().split())

                    # Isolate the exact orphan child processes spawned by our script
                    spawned_pids = pids_after - pids_before

                    for pid in spawned_pids:
                        try:
                            # Send SIGKILL (Signal 9) to forcefully terminate the window instantly
                            os.kill(int(pid), signal.SIGKILL)
                        except Exception:
                            pass
                except Exception:
                    # Fallback global sweep if pgrep hits an operational snag
                    try:
                        subprocess.run(
                            ["pkill", "-9", "-f", "brave-browser"],
                            stdout=subprocess.DEVNULL,
                            stderr=subprocess.DEVNULL,
                        )
                        subprocess.run(
                            ["pkill", "-9", "-f", "brave"],
                            stdout=subprocess.DEVNULL,
                            stderr=subprocess.DEVNULL,
                        )
                    except Exception:
                        pass

        return source_html
