# app/core/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings
from sqlalchemy.ext.declarative import declarative_base  # ← Tambahkan ini


Base = declarative_base()

# Buat engine dari DATABASE_URL dari .env
engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,  # Cek koneksi sebelum query
    echo=settings.DEBUG,  # Log SQL query jika debug=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ✅ Tambahkan baris ini:

def get_db():
    """Dependency untuk FastAPI: inject session ke route"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()