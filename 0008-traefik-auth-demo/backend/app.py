import os
from datetime import datetime, timedelta, timezone

from fastapi import FastAPI, HTTPException, Header
from fastapi.middleware.cors import CORSMiddleware
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel

auth_app = FastAPI()

auth_app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://auth.localhost"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

AUTHDEMO_SERVICE_NAME = os.getenv("AUTHDEMO_SERVICE_NAME", "auth-backend-api")
AUTHDEMO_JWT_SECRET = os.getenv("AUTHDEMO_JWT_SECRET", "demo-secret-key")
JWT_ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

demo_user = {
    "username": "admin",
    "hashed_password": password_context.hash("admin123")
}


class LoginRequest(BaseModel):
    username: str
    password: str


def verify_password(plain_password, hashed_password):
    return password_context.verify(plain_password, hashed_password)


def create_access_token(data: dict):
    token_data = data.copy()
    expire_time = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    token_data.update({"exp": expire_time})

    return jwt.encode(token_data, AUTHDEMO_JWT_SECRET, algorithm=JWT_ALGORITHM)


def verify_token(authorization: str):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing or invalid Authorization header")

    token = authorization.replace("Bearer ", "")

    try:
        payload = jwt.decode(token, AUTHDEMO_JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid or expired token")


@auth_app.get("/")
def root():
    return {
        "message": "Auth backend API is running",
        "service": AUTHDEMO_SERVICE_NAME
    }


@auth_app.post("/login")
def login(login_request: LoginRequest):
    if login_request.username != demo_user["username"]:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    if not verify_password(login_request.password, demo_user["hashed_password"]):
        raise HTTPException(status_code=401, detail="Invalid username or password")

    access_token = create_access_token({"sub": login_request.username})

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


@auth_app.get("/protected")
def protected_route(authorization: str = Header(None)):
    payload = verify_token(authorization)

    return {
        "message": "You have access to protected data",
        "user": payload.get("sub"),
        "service": AUTHDEMO_SERVICE_NAME
    }