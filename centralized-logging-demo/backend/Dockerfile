# Use lightweight Python image
FROM python:3.12-slim

# Set working directory inside the container
WORKDIR /service

# Copy dependency file first for better Docker cache usage
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend application code
COPY backend_logging_service.py .

# Document that the backend listens on port 8000
EXPOSE 8000

# Start FastAPI application with Uvicorn
CMD ["uvicorn", "backend_logging_service:fastapi_logging_app", "--host", "0.0.0.0", "--port", "8000"]