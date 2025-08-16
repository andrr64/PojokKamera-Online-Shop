# app/services/kategori.py
from app.schemas.kategori import KategoriCreate
from app.models.kategori import Kategori
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.exceptions import DuplicateException
from typing import List

class KategoriCRUD:
    @staticmethod
    def create_kategori(kategori: KategoriCreate, db: Session) -> Kategori:
        # cek apakah nama kategori sudah ada (case-insensitive)
        existing = db.query(Kategori).filter(
            func.lower(Kategori.nama) == kategori.nama.lower()
        ).first()
        if existing:
            raise DuplicateException(
                f"Kategori dengan nama '{kategori.nama}' sudah ada."
            )
        
        # buat instance model baru
        db_kategori = Kategori(
            nama=kategori.nama,
            deskripsi=kategori.deskripsi
        )
        db.add(db_kategori)
        db.commit()
        db.refresh(db_kategori)
        return db_kategori
    
    @staticmethod
    def get_all_kategori(db: Session) -> List[Kategori]:
        return db.query(Kategori).all()
    
    @staticmethod
    def delete_kategori(kategori_id: int, db: Session) -> None:
        kategori = db.query(Kategori).filter(Kategori.kategori_id == kategori_id).first()
        if not kategori:
            from app.exceptions import NotFoundException
            raise NotFoundException(f"Kategori dengan id {kategori_id} tidak ditemukan")
        
        db.delete(kategori)
        db.commit()