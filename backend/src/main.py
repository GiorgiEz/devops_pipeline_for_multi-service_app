from fastapi import FastAPI
from .database import create_db_and_tables
from fastapi.middleware.cors import CORSMiddleware
from .routes import books

app = FastAPI()

origins = [
    "http://localhost:8080"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    """
    Event handler to create database and tables on application startup.
    """
    create_db_and_tables()

@app.get("/")
def home():
    return {
        "message": "Welcome to the Book Library API!",
        "docs_url": "http://127.0.0.1:8000/docs"
    }

app.include_router(books.router)
