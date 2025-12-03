from fastapi import FastAPI
from sqlmodel import SQLModel

from db.db import engine
from routers.book import router as book_router

# Base.metadata.create_all(bind=engine) # on startup pydantic will check if table exists and then create one

SQLModel.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(book_router)

@app.get("/")
async def read_root():
    return {"Hello": "World"}

