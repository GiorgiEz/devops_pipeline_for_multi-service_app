from fastapi import FastAPI
from .database import create_db_and_tables
from fastapi.middleware.cors import CORSMiddleware
from .routes import books

app = FastAPI()

origins = [
    "http://localhost:63342",  # your IDE-served frontend
    "http://127.0.0.1:63342"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # safer than "*"
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
