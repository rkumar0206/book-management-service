from fastapi import APIRouter
from models.BookDTO import BookDto as BookDTO

router = APIRouter(prefix="/v1/books", tags=["books"])

@router.get("/", response_model=BookDTO, status_code=200)
async def get_books():
    return {"title": "Hello World"}



