from pydantic import BaseModel, Field


class ParserConfig(BaseModel):
    raw_html_content: str
    max_result: int = Field(default=10, gt=0, le=10)
