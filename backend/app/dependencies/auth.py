# app/dependencies/auth.py
from fastapi import Request, HTTPException, status, Depends
from app.utils.jwt import verify_token

def get_current_user(request: Request) -> dict:

    token = request.cookies.get("access_token")

    if not token:
        auth_header = request.headers.get("Authorization")
        if auth_header and auth_header.startswith("Bearer "):
            token = auth_header.split(" ")[1]

    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized",
        )

    payload = verify_token(token)
    print(payload)
    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized or token expired",
        )

    return payload 
