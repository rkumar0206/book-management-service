from sqlalchemy import Column, Integer, String, Double, Boolean
from db.db import Base

class Book(Base):
    __tablename__ = "book"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title =  Column(String(20), nullable=False)
    author = Column(String(25), nullable=False)
    year = Column(Integer, nullable=True)
    isbn = Column(String(100), nullable=True)
    available = Column(Boolean, default=True, nullable=False)
