# DevOps Pipeline for a Multi-Service Application

## Table of Contents

1. [Project Overview](#project-overview)
2. [Backend (FastAPI)](#backend-fastapi)
3. [Frontend (HTML, CSS, JavaScript)](#frontend-html-css-javascript)
4. [Containerization with Docker](#containerization-with-docker)

   * [Dockerfile for Backend](#dockerfile-for-backend)
   * [Dockerfile for Frontend](#dockerfile-for-frontend)
5. [Docker Compose Integration](#docker-compose-integration)
6. [Running the Application](#running-the-application)
7. [Accessing Services](#accessing-services)

---

## Project Overview

This project demonstrates a full DevOps pipeline for a containerized multi-service application consisting of:

* A **FastAPI** backend that manages a bookstore.
* A **static frontend** using HTML, CSS, and JavaScript.
* Both services containerized with **Docker** and orchestrated via **Docker Compose**.

---

## Backend (FastAPI)

The backend service is built using FastAPI and SQLModel to provide REST APIs to:

* Add a new book
* Retrieve all books
* Retrieve a book by ID
* Delete a book

### Book Model

```python
class Book(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(min_length=1, max_length=50)
    author: str = Field(min_length=1, max_length=50)
    year: int
    genre: Optional[str] = Field(default=None, max_length=50)
```

---

## Frontend (HTML, CSS, JavaScript)

The frontend is a static website built with:

* HTML for structure
* CSS for styling
* JavaScript for fetching and displaying books via the backend API

Features:

* Display all books
* Add a new book
* Delete a book

---

## Containerization with Docker

### Dockerfile for Backend

```dockerfile
FROM python:3.11-slim

# Set working directory to /app
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire backend including src/
COPY . .

# Set working directory inside the container to /app/src
WORKDIR /app/src

# Expose FastAPI's port
EXPOSE 8000

# Run the FastAPI server using `fastapi dev`
CMD ["fastapi", "dev", "main.py", "--host", "0.0.0.0", "--port", "8000"]
```

### Dockerfile for Frontend

```dockerfile
FROM nginx:alpine

# Copy static files to the nginx html directory
COPY . /usr/share/nginx/html

# Expose default NGINX port
EXPOSE 80
```

---

## Docker Compose Integration

A `docker-compose.yml` file orchestrates both services:

```yaml
services:
  backend:
    build: ./backend
    container_name: bookstore-backend
    ports:
      - "8000:8000"
    working_dir: /app/src
    volumes:
      - ./backend:/app
    command: fastapi dev main.py --host 0.0.0.0 --port 8000

  frontend:
    build: ./frontend
    container_name: bookstore-frontend
    ports:
      - "8080:80"
    depends_on:
      - backend
```

---

## Running the Application

To build and run both services:

```bash
# From project root
docker compose up --build
```

---

## Accessing Services

* **Backend (FastAPI):** [http://localhost:8000](http://localhost:8000)
* **FastAPI Docs:** [http://localhost:8000/docs](http://localhost:8000/docs)
* **Frontend (Bookstore UI):** [http://localhost:8080](http://localhost:8080)

---

At this stage, both services are containerized and interact seamlessly via Docker Compose.
