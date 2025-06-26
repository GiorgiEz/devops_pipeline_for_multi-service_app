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
