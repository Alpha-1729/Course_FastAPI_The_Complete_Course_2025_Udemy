#!/usr/bin/python3
# Create Fastapi Endpoint

"""
>>>> Running the fastapi application.
        uvicorn books:app --reload
>>>> Stopping the server.
        Ctrl + C on the terminal
>>>> Other ways to run the fastapi application (If you have the newest version of the fastapi application).

        First install this using pip.
            pip install "fastapi[standard]"

        fastapi run books.py (Run in production mode)
        fastapi dev books.py (Run in development mode)
>>>>
"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def first_api():
    return {"message": "Hello World"}
