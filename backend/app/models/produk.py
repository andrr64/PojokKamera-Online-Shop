# app/models/produk.py
from sqlalchemy import Column, Integer, String, Text, Numeric, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base

class Produk(Base):
    __tablename__ = "produk"

    produk_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nama = Column(String, nullable=False)
    deskripsi = Column(Text, nullable=True)
    harga = Column(Numeric(precision=12, scale=2), nullable=False)  # Misal: 9999999999.99
    stok = Column(Integer, nullable=False)
    kategori_id = Column(Integer, ForeignKey("kategori.kategori_id", ondelete="SET NULL"), nullable=True)
    merek_id = Column(Integer, ForeignKey("merek.merek_id", ondelete="SET NULL"), nullable=True)
    dibuat_pada = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    diperbarui_pada = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )

    # Relasi
    kategori = relationship("Kategori", back_populates="produk")
    merek = relationship("Merek", back_populates="produk")
    ulasan = relationship("Ulasan", back_populates="produk", cascade="all, delete-orphan")
    item_pesanan = relationship("ItemPesanan", back_populates="produk", cascade="all, delete-orphan")
    images = relationship("ProductImages", back_populates="produk", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Produk(id={self.produk_id}, nama='{self.nama}', harga={self.harga})>"