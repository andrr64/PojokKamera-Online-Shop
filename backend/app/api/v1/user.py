# app/api/v1/user.py
from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from app.schemas.user import UserLogin, UserRegister, UserRead
from app.schemas.response import ResponseModel
from app.utils.jwt import create_access_token
from app.core.config import settings
from app.core.database import get_db
from app.services.user import login_user, register_user, login_admin, register_admin
from app.exceptions import AuthenticationException, IntegrityException, DuplicateException

router = APIRouter()

@router.post("/login", response_model=ResponseModel)
def login(req: UserLogin, response: Response, db: Session = Depends(get_db)):
    try:
        user = login_user(db, req)
        token = create_access_token(data={
            "sub": str(user.pengguna_id),
            "role": "user"
        })

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
            detail="Login berhasil",
            data= UserRead.model_validate(user)
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
def register(body: UserRegister, db: Session = Depends(get_db)):
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

from app.dependencies.auth_admin import auth_admin, AdminAuth

# ADMIN
@router.post("/register-admin", response_model=ResponseModel, status_code=status.HTTP_201_CREATED)
def register_admin_ep(
    body: UserRegister, 
    db: Session = Depends(get_db),
    admin: AdminAuth = Depends(auth_admin)
):
    try:
        user = register_admin(db, body, admin.id)
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

@router.post("/login-admin", response_model=ResponseModel)
def login_as_admin(req: UserLogin, response: Response, db: Session = Depends(get_db)):
    try:
        user = login_admin(db, req)
        
        token = create_access_token(data={
            "sub": str(user.pengguna_id),
            "role": "admin"
        })

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
            detail="Login berhasil",
            data = UserRead.model_validate(user)
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