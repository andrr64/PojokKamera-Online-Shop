# app/api/v1/auth.py
from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from app.schemas.auth import LoginRequest, RegisterRequest
from app.schemas.response import ResponseModel
from app.utils.jwt import create_access_token
from app.core.config import settings
from app.core.database import get_db
from app.services.auth import login_user, register_user
from app.exceptions import AuthenticationException, IntegrityException, DuplicateException

router = APIRouter()

@router.post("/login", response_model=ResponseModel)
def login(req: LoginRequest, response: Response, db: Session = Depends(get_db)):
    try:
        user = login_user(db, req)
        token = create_access_token(data={"sub": user.email})

        # Set cookie HTTP-only
        response.set_cookie(
            key="access_token",
            value=token,
            httponly=True,
            secure=False,       # aktifkan kalau HTTPS
            samesite="strict", # cegah CSRF
            max_age=settings.ACCESS_TOKEN_EXPIRE_HOUR * 3600
        )

        return ResponseModel(
            detail="Login berhasil"
        )

    except AuthenticationException as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Terjadi kesalahan internal: {str(e)}"
        )


@router.post("/register", response_model=ResponseModel, status_code=status.HTTP_201_CREATED)
def register(body: RegisterRequest, db: Session = Depends(get_db)):
    try:
        user = register_user(db, body)
        return ResponseModel(
            detail="Registrasi berhasil",
            data={"email": user.email, "username": user.username}
        )

    except IntegrityException:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username atau email tidak valid"
        )
    except DuplicateException:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Username atau email sudah digunakan"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Terjadi kesalahan internal: {str(e)}"
        )
