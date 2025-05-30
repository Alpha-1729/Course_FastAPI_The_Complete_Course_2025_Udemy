#!/usr/bin/python3
# Swagger Pydantic Configurations

"""
>>>>
>>>>
>>>>
>>>>
"""


from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel, Field

app = FastAPI()


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int

    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating


class BookRequest(BaseModel):
    id: Optional[int] = Field(description="Id is not needed on create", default=None, exclude=True)
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=-1, lt=6)

    # Id will not be now auto populated on the swagger.
    # This one is an older syntax.
    # These values will be shown in the swagger as placeholder for each field.
    model_config = {
        "json_scheme_extra": {
            "example": {
                "title": "A new book",
                "author": "test author",
                "description": "A new description of a book",
                "rating": 5,
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
            }
        }
    """


BOOKS = [
    Book(1, "Computer Science Pro", "ruby", "A very nice book", 5),
    Book(2, "Be Fast with FastAPI", "ruby", "A great book", 5),
    Book(3, "Master Endpoints", "ruby", "A awesome book", 5),
    Book(4, "HP1", "Author 1", "Book Description", 2),
    Book(5, "HP2", "Author 2", "Book Description", 3),
    Book(5, "HP3", "Author 3", "Book Description", 1),
]


@app.get("/books/")
async def read_all_books():
    return BOOKS


@app.post("/create-book")
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(find_book_id(new_book))


def find_book_id(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book
