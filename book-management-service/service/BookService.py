from db.model.BookEntity import Book as BookEntity
from models.BookDTO import BookDto


def create_book(payload: BookDto, db):
    book = BookEntity(title=payload.title, author=payload.author, year=payload.year, isbn=payload.isbn, available=payload.available)
    db.add(book)
    db.commit()
    return BookDto(id = book.id, title = book.title, author = book.author, year = book.year, isbn = book.isbn, available = book.available)

def get_books(db) -> list[BookDto]:
    entities = db.query(BookEntity).all()
    return [
        BookDto(id = book.id, title = book.title, author = book.author, year = book.year, isbn = book.isbn, available = book.available)
        for book in entities
    ]

def get_book_by_id(_id, db):
    book = db.query(BookEntity).filter(BookEntity.id == _id).first()
    return BookDto(id = book.id, title = book.title, author = book.author, year = book.year, isbn = book.isbn, available = book.available)

def delete_book(_id, db):
    db.query(BookEntity).filter(BookEntity.id == _id).delete()
    db.commit()

def update_book(_id, payload, db):
    book = db.query(BookEntity).filter(BookEntity.id == _id).first()

    book.title = payload.title
    book.author = payload.author
    book.year = payload.year
    book.isbn = payload.isbn
    book.available = payload.available

    db.commit()

    return BookDto(id = book.id, title = book.title, author = book.author, year = book.year, isbn = book.isbn, available = book.available)
