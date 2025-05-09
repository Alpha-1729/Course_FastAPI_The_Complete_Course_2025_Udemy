from .models import Base
from fastapi import FastAPI
from .database import engine
from .routers import auth, todos, admin, users

app = FastAPI()


@app.get("/healthy")
def health_check():
    return {"status": "Healthy"}


# This will create all the tables for the todos application.
Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(users.router)
