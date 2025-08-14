# app/crud/merek.py
from sqlalchemy.orm import Session
from app.models.merek import Merek
from app.schemas.merek import MerekCreate

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
