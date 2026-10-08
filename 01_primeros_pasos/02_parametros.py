from fastapi import FastAPI

app = FastAPI()

#@app.get("/books")
#async def get_books():
#    return ["1984", "Art of War"]


#@app.get("/books")
#async def get_books2():
#    return ["Harry Potter", "Twilight"]

@app.get("/books/favorite")
async def get_favorite_book():
    return {"title": "1984"}

@app.get("/books/{book_id}")
async def get_book(book_id: int):
    return {"book_id": book_id} 