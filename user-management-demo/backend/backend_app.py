import os
import time
import psycopg2
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# FastAPI application instance
fastapi_app = FastAPI()

# Backend instance name (used to identify which container handled the request)
BACKEND_INSTANCE_NAME = os.getenv("INSTANCE_NAME", "backend")

# Database configuration (loaded from environment variables)
APP_DB_HOST = os.getenv("DB_HOST", "db")
APP_DB_NAME = os.getenv("DB_NAME", "userdemo")
APP_DB_USER = os.getenv("DB_USER", "userdemo")
APP_DB_PASSWORD = os.getenv("DB_PASSWORD", "userdemo")


# Request model for user creation
class UserCreate(BaseModel):
    name: str
    email: str
    password: str


# Request model for user sign-in
class SignIn(BaseModel):
    email: str
    password: str


# Establish database connection with retry mechanism
def get_db_connection(retries=10, delay=2):
    last_error = None

    for attempt in range(retries):
        try:
            return psycopg2.connect(
                host=APP_DB_HOST,
                database=APP_DB_NAME,
                user=APP_DB_USER,
                password=APP_DB_PASSWORD
            )
        except psycopg2.OperationalError as error:
            last_error = error
            print(f"Database is not ready yet. Retry {attempt + 1}/{retries}...")
            time.sleep(delay)

    raise last_error


# Initialize database schema if it does not exist
def initialize_database():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        );
    """)

    conn.commit()
    cur.close()
    conn.close()


# Run database initialization when the application starts
@fastapi_app.on_event("startup")
def on_startup():
    initialize_database()


# Health check endpoint
@fastapi_app.get("/api/v1/health")
def health():
    return {
        "status": "ok",
        "served_by": BACKEND_INSTANCE_NAME
    }


# Create a new user
@fastapi_app.post("/api/v1/users")
def create_user(user: UserCreate):
    try:
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO users (name, email, password) VALUES (%s, %s, %s) RETURNING id;",
            (user.name, user.email, user.password)
        )

        user_id = cur.fetchone()[0]
        conn.commit()

        cur.close()
        conn.close()

        return {
            "message": "User created successfully",
            "user_id": user_id,
            "served_by": BACKEND_INSTANCE_NAME
        }

    except psycopg2.errors.UniqueViolation:
        raise HTTPException(status_code=400, detail="Email already exists")


# Authenticate user
@fastapi_app.post("/api/v1/auth/signin")
def sign_in(data: SignIn):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT id, name, email FROM users WHERE email = %s AND password = %s;",
        (data.email, data.password)
    )

    user = cur.fetchone()

    cur.close()
    conn.close()

    if not user:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    return {
        "message": "Sign in successful",
        "user": {
            "id": user[0],
            "name": user[1],
            "email": user[2]
        },
        "served_by": BACKEND_INSTANCE_NAME
    }


# Retrieve user by email
@fastapi_app.get("/api/v1/users/me")
def get_user(email: str):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT id, name, email FROM users WHERE email = %s;",
        (email,)
    )

    user = cur.fetchone()

    cur.close()
    conn.close()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return {
        "user": {
            "id": user[0],
            "name": user[1],
            "email": user[2]
        },
        "served_by": BACKEND_INSTANCE_NAME
    }


# Delete user by email
@fastapi_app.delete("/api/v1/users/me")
def delete_user(email: str):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM users WHERE email = %s RETURNING id;",
        (email,)
    )

    deleted = cur.fetchone()
    conn.commit()

    cur.close()
    conn.close()

    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")

    return {
        "message": "User deleted successfully",
        "served_by": BACKEND_INSTANCE_NAME
    }