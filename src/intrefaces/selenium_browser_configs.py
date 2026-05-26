from pydantic import BaseModel, Field


class SelenmiumBrowserConfig(BaseModel):
    uc: bool = True
    browser_path: str
    headless: bool = False
