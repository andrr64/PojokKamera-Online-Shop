# app/models/ulasan.py
from sqlalchemy import Column, Integer, ForeignKey, Integer, Text, DateTime, ARRAY, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base

class Ulasan(Base):
    __tablename__ = "ulasan"

    ulasan_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    produk_id = Column(Integer, ForeignKey("produk.produk_id", ondelete="CASCADE"), nullable=False)
    pengguna_id = Column(Integer, ForeignKey("users.pengguna_id", ondelete="CASCADE"), nullable=False)
    bintang = Column(Integer, nullable=False)  # 1-5
    komentar = Column(Text, nullable=True)
    foto = Column(ARRAY(String), nullable=True)  # Simpan path/URL gambar
    dibuat_pada = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    # Relasi
    produk = relationship("Produk", back_populates="ulasan")
    pengguna = relationship("User", back_populates="ulasan")

    def __repr__(self):
        return f"<Ulasan(id={self.ulasan_id}, bintang={self.bintang}, oleh user={self.pengguna_id})>"