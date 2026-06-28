# Google SERP Scraper

 
[![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg?style=flat-square)](https://opensource.org/licenses/MIT)
[![Python: >=3.11](https://img.shields.io/badge/Python->=3.11-3776AB.svg?style=flat-square&logo=python&logoColor=white)](https://www.python.org/downloads/)


A modular, on-demand web crawler built in Python to programmatically extract search engine results pages (SERP) from Google. The tool allows dynamic browser switching, automatically handles anti-bot detection walls via advanced stealth mechanisms, and outputs structured JSON data.

## Features

* **Dynamic Browser Swapping**: Easily switch execution runtimes between Google Chrome, and Brave.
* **Built-in Bot Protection**: Leverages undetected browser automation to bypass tracking cookies and security challenge loops.
* **On-Demand Extraction**: Synchronous pipeline designed to fetch up to 10 organic search results instantly based on user queries.
* **Deterministic Teardown**: Implements kernel-level process management to guarantee no lingering background browser windows or zombie memory leaks on Ubuntu/Linux systems.
* **Clean Data Contracts**: Returns immutable, structured data objects containing page titles and target URLs.

---

## Project Directory Layout

```text
google_scraper/
│
├── config/                  # Global crawler parameters & CSS targets
│   └── settings.py          
│
├── src/                     # Core application source
│   ├── interfaces/          # Contract blueprints for fetching, parsing, and exporting
│   ├── models/              # Immutable Data Transfer Objects (DTO)
│   ├── services/            # Engine implementations (SeleniumBase & BeautifulSoup)
│   ├── factories/           # Runtime instantiation logic for browser swapping
│   └── orchestrator.py      # Main pipeline coordinator
│
├── utils/                   # Stateless technical helper scripts
│   └── uri_utils.py         # Dynamic URL builder and encoder
│
├── tests/                   # Isolated test suite
├── main.py                  # Command-Line Interface (CLI) entry point
└── requirements.txt         # Project dependencies
```

---

# Installation & Setup

This project is built and optimized for Python 3.11+

### System Prerequisites
Because undetected automation configurations require a virtual display surface on Linux, you must install the `xvfb` frame-buffer dependency on your host OS machine:

```bash
sudo apt update && sudo apt install -y xvfb
```

## Installation

This project is not published to PyPI. Install it directly from the Git repository into your virtual environment.

**Using pip:**

```bash
# Clone the repository
git clone https://github.com/shaikhsajid1111/google-serp.git
cd google-serp

# Create and activate a virtual environment (Python >=3.12 required)
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install all dependencies
pip install -r requirements.txt
```

**Using uv (recommended):**

```bash
git clone https://github.com/shaikhsajid1111/google-serp.git
cd google-serp
uv sync
```

> **Linux prerequisite:** The undetected browser automation layer requires a virtual display surface. Install `xvfb` before running:
> ```bash
> sudo apt update && sudo apt install -y xvfb
> ```
> If you encounter X11/Wayland crashes on newer Ubuntu builds, force-reinstall the display wrapper:
> ```bash
> pip install "python-xlib==0.33" --force-reinstall
> ```

---

## Usage

### Interactive CLI

Run the entry-point script directly. You will be prompted to choose a browser and enter your search query:

```bash
python3 main.py
```

**Example session:**

```
Select Browser (chrome/brave): brave
Enter search query: automated web scraping python
```

---

### Programmatic Usage

To embed the scraper in your own script, wire up the four core components — config, fetcher, parser, exporter, and orchestrator — exactly as `main.py` does:

```python
import sys
from src.factories.fetcher_factory import Fetcherfactory
from src.services.parser_html import GoogleSerpParser
from src.orchestrator import GoogleScraperOrchestrator
from src.intrefaces.selenium_browser_configs import SeleniumBrowserConfig
from src.services.json_exporter import JsonExporter

def run_scrape(query: str, browser: str = "chrome") -> list[dict]:
    # 1. Define browser configuration
    config = SeleniumBrowserConfig(
        uc=True,                              # Enable undetected-Chrome stealth mode
        browser_path="/usr/bin/google-chrome",# Absolute path to the browser binary
        headless=False,                       # Run with a visible window
        proxy=None                            # No proxy
    )

    # 2. Instantiate the pipeline components
    fetcher      = Fetcherfactory.create_fetcher(browser)
    parser       = GoogleSerpParser()
    data_exporter = JsonExporter()

    # 3. Build and run the orchestrator
    scraper = GoogleScraperOrchestrator(fetcher, parser, data_exporter)

    # 4. Scrape — returns up to `num_results` organic results as a list of dicts
    results = scraper.scrape(
        query=query,
        num_results=10,
        browser=browser,
        config=config
    )
    return results


if __name__ == "__main__":
    results = run_scrape("python web scraping tutorial", browser="brave")
    print(results)
```

**Sample output:**

```json
[
    {
        "title": "Software Engineer (Full-Stack & Data Engineering)",
        "url": "https://shaikhsajid1111.github.io/portfolio/"
    },
    {
        "title": "Sajid Shaikh",
        "url": "https://dev.to/shaikhsajid1111"
    },
    {
        "title": "Sajid Shaikh - Full stack Developer | HTML5 | CSS3",
        "url": "https://in.linkedin.com/in/sajid-shaikh-66a793201"
    },
    {
        "title": "Sajid Shaikh",
        "url": "https://us.sios.com/leadership/sajid-shaikh/"
    }
]
```
OR `csv`
```csv
title,url
Sajid Shaikh - Software Engineer 2 @Findem | Full-Stack & ...,https://in.linkedin.com/in/shaikhsajid1111
Sajid Shaikh shaikhsajid1111,https://github.com/shaikhsajid1111
Software Engineer (Full-Stack & Data Engineering),https://shaikhsajid1111.github.io/portfolio/
Sajid Shaikh,https://dev.to/shaikhsajid1111
Sajid Shaikh - InfoVision Inc.,https://in.linkedin.com/in/sajid-shaikh-58085915
Sajid-Portfolio,https://connectwithsajid.github.io/
Sajid Sheikh | Software Engineer,https://www.sajid-sheikh.dev/
Sajid Shaikh,https://us.sios.com/leadership/sajid-shaikh/
Sajid Shaikh Email & Phone Number | Findem Software ...,https://rocketreach.co/sajid-shaikh-email_244374012
Sajid Shaikh - Full stack Developer | HTML5 | CSS3,https://in.linkedin.com/in/sajid-shaikh-66a793201
```

---

## Arguments Reference

### `SeleniumBrowserConfig`

Defined in `src/intrefaces/selenium_browser_configs.py`. Passed to `GoogleScraperOrchestrator.scrape()` to control browser behaviour.

| Argument | Type | Default (from `main.py`) | Description |
|---|---|---|---|
| `uc` | `bool` | `True` | Enables **undetected-Chrome** stealth mode via SeleniumBase. When `True`, the browser fingerprint is patched to bypass bot-detection walls (Cloudflare, reCAPTCHA, etc.). |
| `browser_path` | `str` | `"/usr/bin/google-chrome"` | Absolute filesystem path to the browser executable. Use `/usr/bin/brave-browser` for Brave or point to any Chromium-based binary. |
| `headless` | `bool` | `False` | When `True`, launches the browser without a visible GUI window. Requires a virtual display (`xvfb`) on headless Linux servers. |
| `proxy` | `str \| None` | `None` | Optional proxy server URL in the format `"http://user:pass@host:port"`. Pass `None` to disable proxy routing. |

---

### `Fetcherfactory.create_fetcher(browser)`

Defined in `src/factories/fetcher_factory.py`. A factory method that returns the correct fetcher implementation for the selected browser runtime.

| Argument | Type | Accepted Values | Description |
|---|---|---|---|
| `browser` | `str` | `"chrome"`, `"brave"` | Selects the browser engine. Determines which SeleniumBase driver profile and binary is loaded at runtime. Case-sensitive; must match exactly. |

---

### `GoogleScraperOrchestrator.scrape()`

Defined in `src/orchestrator.py`. The main pipeline entry point. Coordinates fetching, HTML parsing, and data export.

| Argument | Type | Default | Description |
|---|---|---|---|
| `query` | `str` | *(required)* | The raw search query string to submit to Google Search (e.g., `"python web scraping"`). URL-encoding is handled internally by `utils/uri_utils.py`. |
| `num_results` | `int` | `10` | Maximum number of organic search results to extract per run. The pipeline is optimised for up to 10 results (one SERP page). |
| `browser` | `str` | *(required)* | Must match the value passed to `Fetcherfactory.create_fetcher()`. Used internally to route browser-specific teardown and process management. |
| `config` | `SeleniumBrowserConfig` | *(required)* | A fully constructed `SeleniumBrowserConfig` instance (see above) that is forwarded to the underlying SeleniumBase fetcher service. |

---

### `config/settings.py` — Global Crawler Parameters

These are module-level constants, not constructor arguments. Edit this file directly to adjust crawler-wide behaviour without touching core logic.

| Constant | Type | Default | Description |
|---|---|---|---|
| `GOOGLE_BASE_URL` | `str` | `"https://google.com"` | The base URL used to construct all Google Search requests. Change to a country-specific domain (e.g., `"https://google.co.uk"`) to localise results. |
| `PAGE_LOAD_TIMEOUT` | `int` | `7` | Seconds the fetcher waits for the Google SERP page to fully load before timing out and raising an exception. Increase on slow or proxied connections. |
| *(CSS selectors)* | `str` | *(repo-defined)* | Additional class/attribute selectors that target Google's organic result elements. Update these when Google changes its HTML structure without needing to touch core source files. |

---

## Output Data Contract

Each scraped result is an immutable data object (Pydantic model, defined in `src/models/`) serialised as a JSON object with exactly two fields:

| Field | Type | Description |
|---|---|---|
| `title` | `str` | The visible link title text of the organic search result. |
| `url` | `str` | The destination URL of the organic search result. |

---

## Configuration Adjustments

If Google updates its underlying web interface design rules, you do not need to modify the core crawler files. Simply adjust your structural class target strings in **`config/settings.py`**:

```python
# config/settings.py

GOOGLE_BASE_URL = "https://google.com"
PAGE_LOAD_TIMEOUT = 7

#more selctors

```
