from fastapi import APIRouter, Query, HTTPException
from typing import Annotated
from ..models import Book
from ..database import SessionDep
from sqlmodel import select


router = APIRouter(prefix="/books", tags=["Books"])

@router.post("/")
def create_book(book: Book, session: SessionDep) -> Book:
    """
    Create a new book in the database.

    Args:
        book (Book): Book data provided in the request body.
        session (SessionDep): SQLModel session dependency.

    Returns:
        Book: The created book with its generated ID.
    """
    session.add(book)
    session.commit()
    session.refresh(book)
    return book

@router.get("/")
def read_books(session: SessionDep, offset: int = 0, limit: Annotated[int, Query(le=100)] = 100) -> list[Book]:
    """
    Retrieve a list of all books with optional pagination.

    Args:
        session (SessionDep): SQLModel session dependency.
        offset (int): Number of records to skip (default: 0).
        limit (int): Maximum number of records to return (default: 100, max: 100).

    Returns:
        list[Book]: A list of books.
    """
    books = session.exec(select(Book).offset(offset).limit(limit)).all()
    return books

@router.get("/{book_id}")
def read_book(book_id: int, session: SessionDep) -> Book:
    """
    Retrieve a single book by its ID.

    Args:
        book_id (int): ID of the book to retrieve.
        session (SessionDep): SQLModel session dependency.

    Returns:
        Book: The book with the specified ID.

    Raises:
        HTTPException: If the book is not found.
    """
    book = session.get(Book, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.delete("/{book_id}")
def delete_book(book_id: int, session: SessionDep):
    """
    Delete a book by its ID.

    Args:
        book_id (int): ID of the book to delete.
        session (SessionDep): SQLModel session dependency.

    Returns:
        dict: A success message if deletion was successful.

    Raises:
        HTTPException: If the book is not found.
    """
    book = session.get(Book, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    session.delete(book)
    session.commit()
    return {"ok": True}
