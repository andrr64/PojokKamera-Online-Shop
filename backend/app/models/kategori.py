# app/models/kategori.py
from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from app.core.database import Base


class Kategori(Base):
    __tablename__ = "kategori"

    kategori_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nama = Column(String(50), unique=True, nullable=False, index=True)
    deskripsi = Column(Text, nullable=True)
    dibuat_pada = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    diperbarui_pada = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )

    def __repr__(self):
        return f"<Kategori(id={self.kategori_id}, nama='{self.nama}')>"