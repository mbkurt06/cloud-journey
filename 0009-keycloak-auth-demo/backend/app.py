from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt
from jose.exceptions import JWTError
import requests
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()
Instrumentator().instrument(app).expose(app)
security = HTTPBearer()

KEYCLOAK_PUBLIC_ISSUER = "http://keycloak.localhost/realms/cloud-journey"
KEYCLOAK_INTERNAL_URL = "http://keycloak:8080/realms/cloud-journey"
JWKS_URL = f"{KEYCLOAK_INTERNAL_URL}/protocol/openid-connect/certs"


def get_jwks():
    try:
        response = requests.get(JWKS_URL, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.RequestException:
        raise HTTPException(
            status_code=503,
            detail="Keycloak JWKS endpoint is not reachable"
        )


def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials

    try:
        header = jwt.get_unverified_header(token)
        jwks = get_jwks()

        rsa_key = None

        for key in jwks["keys"]:
            if key["kid"] == header["kid"]:
                rsa_key = {
                    "kty": key["kty"],
                    "kid": key["kid"],
                    "use": key["use"],
                    "n": key["n"],
                    "e": key["e"],
                }
                break

        if rsa_key is None:
            raise HTTPException(status_code=401, detail="Invalid token key")

        payload = jwt.decode(
            token,
            rsa_key,
            algorithms=["RS256"],
            options={
                "verify_aud": False
            },
            issuer=KEYCLOAK_PUBLIC_ISSUER,
        )

        return payload

    except JWTError:
        raise HTTPException(status_code=401, detail="Token validation failed")


@app.get("/")
def home():
    return {
        "message": "Backend API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/protected")
def protected(payload=Depends(verify_token)):
    return {
        "message": "Protected endpoint",
        "user": payload.get("preferred_username")
    }