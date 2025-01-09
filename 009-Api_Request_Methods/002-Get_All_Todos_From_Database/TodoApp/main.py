import models
from models import Todos
from typing import Annotated
from fastapi import FastAPI, Depends
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

# This will create all the tables for the todos application.
models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


# Dependency injection.
db_dependency = Annotated[Session, Depends(get_db())]


@app.get("/")
async def read_all(db: db_dependency):
    return db.query(Todos).all()
