# app/api/v1/auth.py
from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session
from app.schemas.auth import LoginRequest
from app.utils.jwt import create_access_token
from app.core.config import settings
from app.services.auth import login_user
from app.core.database import get_db
from app.exceptions import AuthenticationException

router = APIRouter()

@router.post("/login", status_code=status.HTTP_200_OK)
def login(req: LoginRequest, response: Response, db: Session = Depends(get_db)):
    try:
        # Verifikasi user & password
        user = login_user(db, req)

        # Buat JWT token
        token = create_access_token(data={"sub": user.email})

        # Set cookie HTTP-only
        response.set_cookie(
            key="access_token",
            value=token,
            httponly=True,
            secure=True,       # aktifkan kalau HTTPS
            samesite="strict", # cegah CSRF
            max_age=settings.ACCESS_TOKEN_EXPIRE_HOUR * 3600
        )

        return {"message": "Login berhasil"}

    except AuthenticationException as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Terjadi kesalahan internal."
        )
