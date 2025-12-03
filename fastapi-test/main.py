# def main():
#     print("Hello from fastapi-test!")
#
#
# if __name__ == "__main__":
#     main()

from fastapi import FastAPI
from routers.book import router as book_router
app = FastAPI()

app.include_router(book_router)

@app.get("/")
async def read_root():
    return {"Hello": "World"}