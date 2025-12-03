from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from typing import Annotated
from models.BookDTO import BookDto as BookDTO
from service import BookService as book_service
from db.db import get_db

router = APIRouter(prefix="/v1/books", tags=["books"])

@router.get("/", response_model=list[BookDTO], status_code=200, summary="Get all books", description="Get all books")
async def get_books(db = Depends(get_db)):
    return book_service.get_books(db)

@router.get("/{book_id}", response_model=BookDTO, status_code=200, summary="Get a book", description="Get a book")
async def get_book(book_id: int, db = Depends(get_db)):
    return book_service.get_book_by_id(book_id, db)

@router.post("/", response_model=BookDTO, status_code=201)
async def create_book_post(
        book_dto: BookDTO,
        db: Annotated[Session, Depends(get_db)]
) -> BookDTO:
    return book_service.create_book(book_dto, db)

@router.put("/{book_id}", status_code=200, summary="Update a book", description="Update a book")
async def update_book(book_id: int, book_dto: BookDTO, db: Annotated[Session, Depends(get_db)]):

    if book_service.get_book_by_id(book_id, db) is None:
        return {"message": "Book not found"}, 404

    return book_service.update_book(book_id, book_dto, db)

@router.delete("/{book_id}", status_code=200, summary="Delete a book", description="Delete a book")
async def delete_book(book_id: int, db: Annotated[Session, Depends(get_db)]):
    if book_service.get_book_by_id(book_id, db) is None:
        return {"message": "Book not found"}, 404

    return book_service.delete_book(book_id, db)




