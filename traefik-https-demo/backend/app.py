from fastapi import FastAPI
import socket

fastapi_https_app = FastAPI()


@fastapi_https_app.get("/")
def root():
    return {
        "message": "HTTPS Backend API is running",
        "instance": socket.gethostname()
    }


@fastapi_https_app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "https-backend-api"
    }