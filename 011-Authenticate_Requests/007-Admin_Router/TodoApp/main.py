import models
from fastapi import FastAPI
from database import engine
from routers import auth, todos, admin

app = FastAPI()

# This will create all the tables for the todos application.
models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
