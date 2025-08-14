from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from app.utils.password import hash_password
from app.schemas.user import UserRole
from sqlalchemy.exc import SQLAlchemyError

# -------------------
# CRUD normal (user-user)
# -------------------

def create_user(db: Session, user: UserCreate) -> User | None:
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
    except SQLAlchemyError as e:
        db.rollback()
        print("Error create_user:", e)
        raise Exception(str(e))

def get_user(db: Session, user_id: int) -> User | None:
    return db.query(User).filter(User.pengguna_id == user_id).first()

def update_user(db: Session, db_user: User, updates: UserUpdate) -> User:
    if updates.username is not None:
        db_user.username = updates.username
    if updates.email is not None:
        db_user.email = updates.email
    if updates.password is not None:
        db_user.password = hash_password(updates.password)
    # normal user tidak bisa ubah peran
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, db_user: User):
    db.delete(db_user)
    db.commit()


# -------------------
# CRUD admin (user-admin)
# -------------------

def admin_get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()

def admin_update_user(db: Session, db_user: User, updates: UserUpdate) -> User:
    # admin bisa update semua field termasuk peran
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

def admin_delete_user(db: Session, db_user: User):
    db.delete(db_user)
    db.commit()
