# app/models/user.py

from sqlalchemy import Column, Integer, String, DateTime, Enum, text
from sqlalchemy.sql import func
from app.core.database import Base

# Enum untuk peran (role)
role_enum = Enum('user', 'admin', name='role_type')

class User(Base):
    __tablename__ = "user"  # Nama tabel di database
    __table_args__ = {"schema": "public"}  # Opsional: bisa dihilangkan jika tidak pakai schema khusus

    # Kolom
    pengguna_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False, index=True)
    password = Column(String, nullable=False)  # Harus sudah di-hash
    peran = Column(role_enum, nullable=False, default='pelanggan')
    dibuat_pada = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    diperbarui_pada = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )

    # Representasi untuk debugging
    def __repr__(self):
        return f"<User(id={self.pengguna_id}, username='{self.username}', email='{self.email}', role='{self.peran}')>"