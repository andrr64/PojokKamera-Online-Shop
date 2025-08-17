# app/services/auth.py
from sqlalchemy.orm import Session
from app.schemas.user import UserLogin
from app.crud.user import UserCRUD
from app.utils.password import verify_password
from app.exceptions import AuthenticationException
from app.schemas.user import UserCreate
from app.models.user import User

def login_admin(db: Session, data: UserLogin) -> User:
    user = UserCRUD.get_admin_by_email(db, data.email)
    if not user:
        raise AuthenticationException("Email atau password salah")

    # Verifikasi password
    if not verify_password(data.password, user.password):
        raise AuthenticationException("Email atau password salah")

    return user

def login_user(db: Session, data: UserLogin) -> User:
    # Ambil user berdasarkan email
    user = UserCRUD.get_by_email(db, data.email)
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
    return UserCRUD.create(db, user_create)


def register_admin(db: Session, body: UserCreate, admin_id):
    # TODO: logging adminid
    user_create = UserCreate(
        username=body.username,
        email=body.email,
        password=body.password
    )
    return UserCRUD.create_admin(db, user_create)
