# app/services/auth.py
from sqlalchemy.orm import Session
from app.schemas.user import UserLogin, UserRegister
from app.crud.user import get_user_by_email
from app.utils.password import verify_password
from app.exceptions import AuthenticationException
from app.crud.user import create_user
from app.schemas.user import UserCreate

def login_user(db: Session, data: UserLogin):
    # Ambil user berdasarkan email
    user = get_user_by_email(db, data.email)
    if not user:
        raise AuthenticationException("Email atau password salah")

    # Verifikasi password
    if not verify_password(data.password, user.password):
        raise AuthenticationException("Email atau password salah")

    return user

def register_user(db: Session, body: UserCreate):
    user_create = UserCreate(
        username=body.username,
        email=body.email,
        password=body.password
    )
    return create_user(db, user_create)
