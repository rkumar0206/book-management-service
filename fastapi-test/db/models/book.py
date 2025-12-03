from sqlalchemy import Column, Integer, String, Double, Boolean
from sqlmodel import Field, SQLModel
# from db.db import Base

# class Book(Base):
#     __tablename__ = "book"
#     id = Column(Integer, primary_key=True)
#     title =  Column(String(100), nullable=False)
#     author = Column(String(100), nullable=False)
#     price = Column(Double, nullable=True)
#     is_published = Column(Boolean, nullable=True)


class BookBase(SQLModel):
    title: str = Field(default="", description="Title of the book")
    author: str = Field(default="", description="Author of the book")

class Book(BookBase, table=True):
    id: int = Field(default=None, primary_key=True)