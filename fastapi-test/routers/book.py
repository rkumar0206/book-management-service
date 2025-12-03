from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.db import get_db
from db.models.book import Book
from services import book_service

router = APIRouter(prefix="/books", tags=["Books"])

@router.get("/{id}", response_model=Book, summary="Get a book by ID")
def get_book_by_id(id: int, db = Depends(get_db)):
    return book_service.get_book_by_id(id, db)

# # pydanitc automatic conversion to response model from dictionary
# @router.get("/pydanitc/{id}",
#             response_model=Book,
#             summary="Get a book by ID"
#             )
# def get_book_by_id_with_pydantic_conversion(id: int, db = Depends(get_db)):
#     book = {
#         "id": id,
#         "title": "Book 2",
#         "author": "someone",
#         "is_published": True
#     }
#     return book


@router.get("/", response_model=list[Book], summary="Get all books")
async def get_books(db = Depends(get_db)):
    return book_service.get_all_books(db)

@router.post(
    "",
    status_code=201,
    summary="Create a new book",
)
async def create_book(book: Book, db: Annotated[Session, Depends(get_db)]):
    return book_service.create_book(book, db)