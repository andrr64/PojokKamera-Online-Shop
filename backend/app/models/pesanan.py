# app/models/pesanan.py
from sqlalchemy import Column, Integer, ForeignKey, Numeric, DateTime, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base

# Enum status pesanan
status_enum = Enum('pending', 'dibayar', 'dikirim', 'selesai', 'dibatalkan',
                   name='status_pesanan')

class Pesanan(Base):
    __tablename__ = "pesanan"

    pesanan_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    pengguna_id = Column(Integer, ForeignKey("users.pengguna_id", ondelete="CASCADE"), nullable=False)
    alamat_id = Column(Integer, ForeignKey("alamat.alamat_id", ondelete="SET NULL"), nullable=True)
    total_harga = Column(Numeric(precision=12, scale=2), nullable=False)
    status = Column(status_enum, nullable=False, default='pending')
    dibuat_pada = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    diperbarui_pada = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )

    # Relasi
    pengguna = relationship("User", back_populates="pesanan")
    alamat = relationship("Alamat", back_populates="pesanan")
    item_pesanan = relationship("ItemPesanan", back_populates="pesanan", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Order(id={self.pesanan_id}, status='{self.status}', total={self.total_harga})>"