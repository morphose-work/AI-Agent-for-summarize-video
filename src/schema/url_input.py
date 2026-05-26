from pydantic import BaseModel, Field

class UrlInputSchema(BaseModel):
    url: str = Field(
        ...,
        description='URL Youtube видео'
    )