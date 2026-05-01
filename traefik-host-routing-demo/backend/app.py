from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import socket

fastapi_backend_app = FastAPI()

fastapi_backend_app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://app.localhost"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

SERVICE_NAME = os.getenv("HOSTROUTING_SERVICE_NAME", "backend-api")


class User(BaseModel):
    name: str
    email: str


@fastapi_backend_app.get("/")
def root():
    return {
        "message": "Backend API is running",
        "service": SERVICE_NAME,
        "instance": socket.gethostname()
    }


@fastapi_backend_app.post("/users")
def create_user(user: User):
    return {
        "message": "User created successfully",
        "user": user,
        "service": SERVICE_NAME,
        "instance": socket.gethostname()
    }