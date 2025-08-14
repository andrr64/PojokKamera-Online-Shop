# app/models/merek.py
from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base

class Merek(Base):
    __tablename__ = "merek"

    merek_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nama = Column(String, unique=True, nullable=False, index=True)
    deskripsi = Column(Text, nullable=True)
    logo = Column(String, nullable=False)
    dibuat_pada = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    diperbarui_pada = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )

    # Relasi
    produk = relationship("Produk", back_populates="merek", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Merek(id={self.merek_id}, nama='{self.nama}')>"