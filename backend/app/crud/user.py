# app/crud/user.py
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
from app.utils.password import hash_password
from app.exceptions import IntegrityException


def create_user(db: Session, user: UserCreate) -> User:
    """
    Membuat user baru. 
    Raises:
        IntegrityException: Jika email atau username sudah digunakan.
    """
    # Cek email sudah ada
    existing_by_email = db.query(User).filter(User.email == user.email).first()
    if existing_by_email:
        raise IntegrityException(f"Email '{user.email}' sudah digunakan.")

    # Cek username sudah ada
    existing_by_username = db.query(User).filter(User.username == user.username).first()
    if existing_by_username:
        raise IntegrityException(f"Username '{user.username}' sudah digunakan.")

    # Hash password
    hashed_pw = hash_password(user.password)

    # Buat user baru
    db_user = User(
        username=user.username,
        email=user.email,
        password=hashed_pw,
        peran=user.peran
    )

    # Simpan ke database
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user