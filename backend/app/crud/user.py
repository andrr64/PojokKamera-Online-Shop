from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from app.utils.password import hash_password
from app.exceptions import DuplicateException, IntegrityException
from app.enum.user_role import RoleEnum

class UserCRUD:
    
    # CRUD ADMIN
    @staticmethod
    def create_admin(db: Session, user: UserCreate) -> User:
        try:
            db_user = User(
                username=user.username,
                email=user.email,
                password=hash_password(user.password),
                peran=RoleEnum.admin
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

    # -------------------
    # CRUD normal (user-user)
    # -------------------
    @staticmethod
    def create(db: Session, user: UserCreate) -> User:
        try:
            db_user = User(
                username=user.username,
                email=user.email,
                password=hash_password(user.password),
                peran=RoleEnum.user
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

    @staticmethod
    def update(db: Session, db_user: User, updates: UserUpdate) -> User:
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
                raise DuplicateException("Username sudah digunakan")
            elif 'users_email_key' in str(e.orig):
                raise DuplicateException("Email sudah digunakan")
            else:
                raise IntegrityException(str(e))

    @staticmethod
    def delete(db: Session, db_user: User):
        try:
            db.delete(db_user)
            db.commit()
        except Exception as e:
            db.rollback()
            raise IntegrityException(str(e))

    @staticmethod
    def get_by_email(db: Session, email: str) -> User | None:
        return db.query(User).filter(User.email == email).first()
    
    @staticmethod
    def get_admin_by_email(db: Session, email: str) -> User | None:
        return db.query(User).filter(
            User.email == email,
            User.peran == RoleEnum.admin
        ).first()
    
    @staticmethod
    def get_by_id(db: Session, user_id: int) -> User | None:
        return db.query(User).filter(User.pengguna_id == user_id).first()

    @staticmethod
    def get_all(db: Session) -> list[User]:
        return db.query(User).all()
