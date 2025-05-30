#!/usr/bin/python3
# Http Exceptions

"""
>>>> HttpException
        It is something we have to raise within our method, which will cancel the functionality of our method and return a message in a status code back to the user.
>>>>
>>>>
>>>>
"""


from fastapi import FastAPI, Path, Query, HTTPException
from typing import Optional
from pydantic import BaseModel, Field

app = FastAPI()


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    published_date: int

    def __init__(self, id, title, author, description, rating, published_date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date


class BookRequest(BaseModel):
    id: Optional[int] = Field(description="Id is not needed on create", default=None)
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=-1, lt=6)
    published_date: int = Field(gt=1999, lt=2031)

    # Id will not be now auto populated on the swagger.
    # These values will be shown in the swagger as placeholder for each field.
    model_config = {
        "json_scheme_extra": {
            "example": {
                "title": "A new book",
                "author": "test author",
                "description": "A new description of a book",
                "rating": 5,
                "published_date": 2029,
            }
        }
    }

    """
    Use this to avoid id in the swagger UI instead of the above.
    The above one is the old syntax.
    class Config:  # Use class Config for better schema configuration
        json_schema_extra = {
            "example": {
                "title": "A new book",
                "author": "test author",
                "description": "A new description of a book",
                "rating": 5,
                "published_date": 2029,
            }
        }
    """


BOOKS = [
    Book(1, "Computer Science Pro", "ruby", "A very nice book", 5, 2012),
    Book(2, "Be Fast with FastAPI", "ruby", "A great book", 5, 2020),
    Book(3, "Master Endpoints", "ruby", "A awesome book", 5, 2010),
    Book(4, "HP1", "Author 1", "Book Description", 2, 2005),
    Book(5, "HP2", "Author 2", "Book Description", 3, 2000),
    Book(5, "HP3", "Author 3", "Book Description", 1, 2006),
]


@app.get("/books")
async def read_all_books():
    return BOOKS


@app.get("/books/{book_id}")
async def read_book(book_id: int = Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book

    raise HTTPException(status_code=404, detail="Item not found")


@app.get("/books/")
async def read_book_by_rating(book_rating: int = Query(gt=0, lt=6)):
    books_to_return = []
    for book in BOOKS:
        if book.rating == book_rating:
            books_to_return.append(book)
    return books_to_return


@app.post("/create-book")
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(find_book_id(new_book))


def find_book_id(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book


@app.put("/books/update_book")
async def update_book(book: BookRequest):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book
            book_changed = True

    if not book_changed:
        raise HTTPException(status_code=404, detail="Item not found")


@app.delete("/books/{book_id}")
async def delete_book(book_id: int = Path(gt=0)):
    book_deleted = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            book_deleted = True
            break

    if not book_deleted:
        raise HTTPException(status_code=404, detail="Item not found")


@app.get("/books/publish/")
async def get_book_by_publish_date(publish_date: int = Query(gt=1999, lt=2031)):
    books_to_return = []
    for book in BOOKS:
        if book.published_date == publish_date:
            books_to_return.append(book)

    return books_to_return
