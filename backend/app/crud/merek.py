# app/crud/merek.py
from sqlalchemy.orm import Session
from app.models.merek import Merek
from app.schemas.merek import MerekCreate
from sqlalchemy import and_

class MerekCRUD:
    @staticmethod
    def create_merek(db: Session, merek_data: MerekCreate) -> Merek:
        # cek duplikat
        existing = db.query(Merek).filter(Merek.nama == merek_data.nama).first()
        if existing:
            raise ValueError("Merek sudah ada")

        # buat instance ORM dari schema
        db_merek = Merek(
            nama=merek_data.nama,
            deskripsi=merek_data.deskripsi,
            logo=merek_data.logo
        )

        db.add(db_merek)
        db.commit()
        db.refresh(db_merek)  # refresh harus model ORM
        return db_merek


    @staticmethod
    def get_all_merek(db: Session):
        return db.query(Merek).all()
    
    @staticmethod
    def get_merek_by_id(db: Session, merek_id: int) -> Merek | None:
        return db.query(Merek).filter(Merek.merek_id == merek_id).first()   
    
    @staticmethod
    def update_merek(db: Session, merek_id: int, merek_data: MerekCreate) -> Merek:
        # cari merek berdasarkan ID
        db_merek = db.query(Merek).filter(Merek.merek_id == merek_id).first()
        if not db_merek:
            raise ValueError("Merek tidak ditemukan")

        # cek nama duplikat (hanya jika nama diubah)
        if merek_data.nama and merek_data.nama != db_merek.nama:
            existing = db.query(Merek).filter(
                and_(Merek.nama == merek_data.nama, Merek.merek_id != merek_id)
            ).first()
            if existing:
                raise ValueError(f"Nama merek '{merek_data.nama}' sudah digunakan")

        # update field yang ada
        if merek_data.nama is not None:
            db_merek.nama = merek_data.nama
        if merek_data.deskripsi is not None:
            db_merek.deskripsi = merek_data.deskripsi
        if merek_data.logo is not None:
            db_merek.logo = merek_data.logo

        db.commit()
        db.refresh(db_merek)
        return db_merek