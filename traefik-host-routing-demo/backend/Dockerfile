# Use a lightweight Python image for the backend API service
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /backend-service

# Copy dependency file first to use Docker layer caching efficiently
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend API source code
COPY app.py .

# Document that the backend API listens on port 8000
EXPOSE 8000

# Start the FastAPI application with Uvicorn
CMD ["uvicorn", "app:fastapi_backend_app", "--host", "0.0.0.0", "--port", "8000"]