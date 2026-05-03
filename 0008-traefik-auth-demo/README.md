# Traefik Auth Demo

## Purpose

This project demonstrates how to implement authentication and authorization using JWT in a containerized environment with Traefik.

The project covers:

- Reverse proxy routing with Traefik
- Frontend login flow
- Backend authentication with FastAPI
- JWT (JSON Web Token) generation
- Protected API endpoints
- Bearer token usage
- Basic CORS handling

---

## Architecture

```bash
Browser
  |
  | http://auth.localhost
  v
Traefik :80
  |
  ├── Frontend (Nginx)
  └── Backend API (FastAPI)
```

Authentication flow:

```bash
User → Login form
     → Backend /login
     → JWT token
     → Frontend stores token
     → Protected API call with Authorization header
```

---

## Project Structure

```bash
0008-traefik-auth-demo/
├── docker-compose.yml
├── frontend/
│   └── index.html
└── backend/
    ├── Dockerfile
    ├── requirements.txt
    └── app.py
```

---

## Services

### Traefik

- Acts as reverse proxy
- Routes traffic based on host rules
- Entry point: `http://auth.localhost`

### Frontend

- Served via Nginx
- Provides login form and API interaction

### Backend API

- Built with FastAPI
- Handles authentication and token generation
- Verifies JWT for protected routes

---

## Authentication Flow

### Step 1 – Login

```bash
POST /login
```

Request:

```json
{
  "username": "admin",
  "password": "admin123"
}
```

Response:

```json
{
  "access_token": "...",
  "token_type": "bearer"
}
```

---

### Step 2 – Access Protected Endpoint

```bash
GET /protected
Authorization: Bearer <token>
```

Response:

```json
{
  "message": "You have access to protected data",
  "user": "admin",
  "service": "auth-backend-api"
}
```

---

## Demo Credentials

```text
username: admin
password: admin123
```

---

## Run the Project

```bash
docker compose down --remove-orphans
docker compose up -d --build
```

---

## Test in Browser

Open:

```bash
http://auth.localhost
```

Steps:

1. Click **Login**
2. Token will appear
3. Click **Call Protected API**
4. Protected response will be displayed

---

## Test via cURL

Login:

```bash
curl -X POST http://api.auth.localhost/login \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","password":"admin123"}'
```

Use token:

```bash
curl http://api.auth.localhost/protected \
  -H "Authorization: Bearer <TOKEN>"
```

---

## Key Concepts Learned

- JWT (JSON Web Token)
- Stateless authentication
- Password hashing with bcrypt
- Token-based authorization
- FastAPI backend authentication
- Reverse proxy routing with Traefik
- Frontend to backend communication
- CORS basics

---

## Important Notes

- This project uses a simple in-memory user for demonstration
- JWT is generated inside the backend
- No database is used
- Not production-ready

---

## Production Considerations

In real-world systems:

- Authentication is handled by a dedicated service (e.g. Keycloak, Auth0)
- Backend services only verify tokens
- Tokens include more claims (roles, permissions)
- Secure storage and rotation of secrets is required

---

## Conclusion

This project demonstrates a full authentication flow using JWT in a microservices-like setup with Traefik.

It forms a strong foundation for:

- API security
- Identity management
- Advanced authentication systems
- Transition to external identity providers