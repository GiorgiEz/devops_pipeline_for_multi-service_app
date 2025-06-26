# database.py

# This setup is adapted from the official SQLModel documentation:
# https://fastapi.tiangolo.com/tutorial/sql-databases/

from typing import Annotated
from fastapi import Depends
from sqlmodel import Session, SQLModel, create_engine

# SQLite database file name
sqlite_file_name = "database.db"

# SQLite connection URL
sqlite_url = f"sqlite:///{sqlite_file_name}"

# Required for SQLite when using it with FastAPI (single-threaded async context)
connect_args = {"check_same_thread": False}

# Create the SQLAlchemy engine
engine = create_engine(sqlite_url, connect_args=connect_args)

# Function to create the database and all tables based on SQLModel models
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# Dependency to provide a database session for each request
def get_session():
    with Session(engine) as session:
        yield session

# Annotated type to use this dependency easily in routes
SessionDep = Annotated[Session, Depends(get_session)]
