# Google SERP Scraper

 
![Open Source Love](https://shields.io) ![License: MIT](https://shields.io) ![Built with Python](https://shields.io)

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

## Installation & Setup

This project is built and optimized for Python 3.11+ on Ubuntu Desktop.

### 1. System Prerequisites
Because undetected automation configurations require a virtual display surface on Linux, you must install the `xvfb` frame-buffer dependency on your host OS machine:

```bash
sudo apt update && sudo apt install -y xvfb
```

### 2. Install Project Dependencies
Clone this repository to your workspace, set up a virtual environment, and install the library stack:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

*Note: If you run into X11 or Wayland version crashes on newer Ubuntu builds, force install the verified display control mapping wrapper:*
```bash
pip install "python-xlib==0.33" --force-reinstall
```

---

## How to Run

Execute the entry-point script directly from your terminal. The script will guide you through dynamic browser targets and string criteria input options:

```bash
python3 main.py
```

### Prompt Example:
```text
Select Browser (chrome/brave): brave
Enter search query: automated web scraping python
```

---

## Sample Output Format

Upon successful execution, the scraping engine coordinates the data workflow pipeline and prints out formatted structural serialization maps:

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
OR
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

## Configuration Adjustments

If Google updates its underlying web interface design rules, you do not need to modify the core crawler files. Simply adjust your structural class target strings in **`config/settings.py`**:

```python
# config/settings.py

GOOGLE_BASE_URL = "https://google.com"
PAGE_LOAD_TIMEOUT = 7

#more selctors

```
