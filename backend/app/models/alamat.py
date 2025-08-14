from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.core.database import Base

class Alamat(Base):
    __tablename__ = "alamat"

    alamat_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    pengguna_id = Column(Integer, ForeignKey("users.pengguna_id", ondelete="CASCADE"), nullable=False)
    label = Column(String, nullable=False)  # e.g., "Rumah", "Kantor"
    jalan = Column(String, nullable=False)
    kota = Column(String, nullable=False)
    provinsi = Column(String, nullable=False)
    kode_pos = Column(String, nullable=False)
    negara = Column(String, nullable=False, default="Indonesia")
    dibuat_pada = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    diperbarui_pada = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )

    # Relasi
    pengguna = relationship("User", back_populates="alamat")
    pesanan = relationship("Pesanan", back_populates="alamat", uselist=False)

    def __repr__(self):
        return f"<Alamat(id={self.alamat_id}, label='{self.label}', kota='{self.kota}')>"