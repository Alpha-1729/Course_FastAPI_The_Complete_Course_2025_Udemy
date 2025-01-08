#!/usr/bin/python3
# Fast Api Assignment And Solution

"""
>>>> Question
        1. Create a new API Endpoint that can fetch all books from a specific author using either Path Parameters or Query Parameters.
>>>>
>>>>
>>>>
"""

from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {"title": "Title One", "author": "Author One", "category": "science"},
    {"title": "Title Two", "author": "Author Two", "category": "science"},
    {"title": "Title Three", "author": "Author Three", "category": "history"},
    {"title": "Title Four", "author": "Author Four", "category": "math"},
    {"title": "Title Five", "author": "Author Five", "category": "math"},
    {"title": "Title Six", "author": "Author Two", "category": "math"},
]


@app.get("/books/byauthor/{author_name}")
async def read_book_by_author(author_name: str):
    books_to_return = []

    for book in BOOKS:
        if book.get("author").casefold() == author_name.casefold():
            books_to_return.append(book)

    return books_to_return
