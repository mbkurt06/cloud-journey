import os
import time
import psycopg2
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

INSTANCE_NAME = os.getenv("INSTANCE_NAME", "backend")

DB_HOST = os.getenv("DB_HOST", "db")
DB_NAME = os.getenv("DB_NAME", "userdemo")
DB_USER = os.getenv("DB_USER", "userdemo")
DB_PASSWORD = os.getenv("DB_PASSWORD", "userdemo")


class UserCreate(BaseModel):
    name: str
    email: str
    password: str


class SignIn(BaseModel):
    email: str
    password: str


def get_connection(retries=10, delay=2):
    last_error = None

    for attempt in range(retries):
        try:
            return psycopg2.connect(
                host=DB_HOST,
                database=DB_NAME,
                user=DB_USER,
                password=DB_PASSWORD
            )
        except psycopg2.OperationalError as error:
            last_error = error
            print(f"Database is not ready yet. Retry {attempt + 1}/{retries}...")
            time.sleep(delay)

    raise last_error


def init_db():
    conn = get_connection()
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


@app.on_event("startup")
def startup():
    init_db()


@app.get("/api/v1/health")
def health():
    return {
        "status": "ok",
        "served_by": INSTANCE_NAME
    }


@app.post("/api/v1/users")
def create_user(user: UserCreate):
    try:
        conn = get_connection()
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
            "served_by": INSTANCE_NAME
        }

    except psycopg2.errors.UniqueViolation:
        raise HTTPException(status_code=400, detail="Email already exists")


@app.post("/api/v1/auth/signin")
def sign_in(data: SignIn):
    conn = get_connection()
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
        "served_by": INSTANCE_NAME
    }


@app.get("/api/v1/users/me")
def get_user(email: str):
    conn = get_connection()
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
        "served_by": INSTANCE_NAME
    }


@app.delete("/api/v1/users/me")
def delete_user(email: str):
    conn = get_connection()
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
        "served_by": INSTANCE_NAME
    }