# Use a lightweight official Python image
FROM python:3.12-slim

# Set working directory inside the container
WORKDIR /app

# Copy dependency list first to leverage Docker layer caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source code into the container
COPY backend_app.py .

# Document that the application listens on port 8000
EXPOSE 8000

# Start the FastAPI application using Uvicorn
# --host 0.0.0.0 ensures the FastAPI application (fastapi_app) is accessible from outside the container
CMD ["uvicorn", "backend_app:fastapi_app", "--host", "0.0.0.0", "--port", "8000"]