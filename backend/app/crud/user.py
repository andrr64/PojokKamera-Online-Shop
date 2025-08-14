# app/crud/user.py
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate, UserRole
from app.utils.password import hash_password
from app.exceptions import DuplicateException, IntegrityException

# -------------------
# CRUD normal (user-user)
# -------------------

def create_user(db: Session, user: UserCreate) -> User:
    try:
        db_user = User(
            username=user.username,
            email=user.email,
            password=hash_password(user.password),
            peran=UserRole.USER
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except IntegrityError as e:
        db.rollback()
        # Cek apakah error karena username atau email duplikat
        if 'users_username_key' in str(e.orig):
            raise DuplicateException(f"Username '{user.username}' sudah digunakan")
        elif 'users_email_key' in str(e.orig):
            raise DuplicateException(f"Email '{user.email}' sudah digunakan")
        else:
            raise IntegrityException(str(e))
    except Exception as e:
        db.rollback()
        raise IntegrityException(str(e))

def update_user(db: Session, db_user: User, updates: UserUpdate) -> User:
    try:
        if updates.username is not None:
            db_user.username = updates.username
        if updates.email is not None:
            db_user.email = updates.email
        if updates.password is not None:
            db_user.password = hash_password(updates.password)
        db.commit()
        db.refresh(db_user)
        return db_user
    except IntegrityError as e:
        db.rollback()
        if 'users_username_key' in str(e.orig):
            raise DuplicateException(f"Username sudah digunakan")
        elif 'users_email_key' in str(e.orig):
            raise DuplicateException(f"Email sudah digunakan")
        else:
            raise IntegrityException(str(e))

def delete_user(db: Session, db_user: User):
    try:
        db.delete(db_user)
        db.commit()
    except Exception as e:
        db.rollback()
        raise IntegrityException(str(e))

def get_user_by_email(db: Session, email: str) -> User | None:
    return db.query(User).filter(User.email == email).first()

# -------------------
# CRUD admin (user-admin)
# -------------------

def admin_get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()

def admin_update_user(db: Session, db_user: User, updates: UserUpdate) -> User:
    try:
        if updates.username is not None:
            db_user.username = updates.username
        if updates.email is not None:
            db_user.email = updates.email
        if updates.password is not None:
            db_user.password = hash_password(updates.password)
        if updates.peran is not None:
            db_user.peran = updates.peran
        db.commit()
        db.refresh(db_user)
        return db_user
    except IntegrityError as e:
        db.rollback()
        if 'users_username_key' in str(e.orig):
            raise DuplicateException(f"Username '{updates.username}' sudah digunakan")
        elif 'users_email_key' in str(e.orig):
            raise DuplicateException(f"Email '{updates.email}' sudah digunakan")
        else:
            raise IntegrityException(str(e))

def admin_delete_user(db: Session, db_user: User):
    try:
        db.delete(db_user)
        db.commit()
    except Exception as e:
        db.rollback()
        raise IntegrityException(str(e))
