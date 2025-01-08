from fastapi import FastAPI
import models
from database import engine

app = FastAPI()

# This will create all the tables for the todos application.
models.Base.metadata.create_all(bind=engine)
