from pydantic import BaseModel, Field
from typing import Optional

class SeleniumBrowserConfig(BaseModel):
    uc: bool = True
    browser_path: str
    headless: bool = False
    proxy: Optional[str] = None
