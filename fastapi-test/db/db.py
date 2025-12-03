# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
#
# Base = declarative_base()
# engine = create_engine("sqlite:///books.db", echo=True)
# SessionLocal = sessionmaker(bind=engine)
#
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db # check it online python concept what yield does
#     finally:
#         db.close()
from typing import Generator

# ---------------------- Using SQL model -------------------

from sqlmodel import create_engine, Session

engine = create_engine("sqlite:///books_sql_model.db", echo=True)

def get_db() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session