from fastapi import APIRouter

router = APIRouter(prefix="/books", tags=["Books"])

@router.get("/{id}")
async def get_books(id: int):
    return {"id": id}