# app/models/item_pesanan.py
from sqlalchemy import Column, Integer, ForeignKey, Numeric, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base

class ItemPesanan(Base):
    __tablename__ = "item_pesanan"

    item_pesanan_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    pesanan_id = Column(Integer, ForeignKey("pesanan.pesanan_id", ondelete="CASCADE"), nullable=False)
    produk_id = Column(Integer, ForeignKey("produk.produk_id", ondelete="SET NULL"), nullable=True)
    jumlah = Column(Integer, nullable=False)
    harga = Column(Numeric(precision=12, scale=2), nullable=False)  # Harga saat pembelian
    dibuat_pada = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    # Relasi
    pesanan = relationship("Pesanan", back_populates="item_pesanan")
    produk = relationship("Produk", back_populates="item_pesanan")

    def __repr__(self):
        return f"<ItemPesanan(id={self.item_pesanan_id}, pesanan={self.pesanan_id}, produk={self.produk_id}, jumlah={self.jumlah})>"