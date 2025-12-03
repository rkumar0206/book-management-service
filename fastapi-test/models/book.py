from pydantic import BaseModel, Field


class Book(BaseModel):
    id: int
    title: str = Field(default='Not Available', min_length=3)
    author: str | None = None
    price: float = 10.00
    is_published: bool = True