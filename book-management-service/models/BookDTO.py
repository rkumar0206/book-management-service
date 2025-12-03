from pydantic import BaseModel, Field

class BookDto(BaseModel):
    id: int | None = None
    title: str = Field(max_length=15)
    author: str = Field(max_length=20)
    year: int | None = None
    isbn: str | None = None
    available: bool = Field(default=True)
