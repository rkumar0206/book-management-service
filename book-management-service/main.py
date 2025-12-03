from fastapi import FastAPI
from router.BookRouter import router as book_router
from db.db import engine
from db.db import Base

app = FastAPI()

app.include_router(book_router)

Base.metadata.create_all(bind=engine)


@app.get("/")
async def root():
    return {"message": "Hello World"}

