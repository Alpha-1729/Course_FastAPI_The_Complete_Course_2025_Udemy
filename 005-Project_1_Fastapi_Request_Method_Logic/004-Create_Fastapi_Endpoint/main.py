#!/usr/bin/python3
# Create Fastapi Endpoint

"""
>>>> Running the fastapi application.
        uvicorn scriptName:appName --reload
        uvicorn main:app --reload
>>>> Stopping the server.
        Ctrl + C on the terminal
>>>> Other ways to run the fastapi application
        If you have the newest version of the fastapi application

        First install this using pip.
            pip install "fastapi[standard]"

        fastapi run main.py (Run in production mode)
        fastapi dev main.py (Run in development mode)
>>>> Uvicorn
        Univorn is a web server we used to start a fastapi application.
"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def first_api():
    return {"message": "Hello World"}
