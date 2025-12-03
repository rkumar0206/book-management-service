from sqlalchemy import Integer
from sqlmodel import select

from db.models.book import Book


# from models.book import Book as BookDTO
# from db.models.book import Book as BookEntity
#
#
# def create_book(payload: BookDTO, db):
#     book = BookEntity(id=payload.id, title=payload.title, author=payload.author, price=payload.price, is_published=payload.is_published)
#     db.add(book)
#     db.commit()
#     db.refresh(book)
#     return book
#
# def get_book_by_id(_id: int, db):
#     return db.query(BookEntity).filter(BookEntity.id == _id).first()
#
# def get_all_books(db):
#     return db.query(BookEntity).all()

# -------------------------- SQLModel -----------------

def create_book(book: Book, db):
    db.add(book)
    db.commit()
    db.refresh(book)
    return book

def get_book_by_id(_id: int, db):
    # statement = select(Book).where(Book.id == _id)
    # return db.exec(statement).first()
    book = db.get(Book, _id) # will only work for the primary key column
    return book

def get_all_books(db):
    statement = select(Book)
    return db.exec(statement).all()

