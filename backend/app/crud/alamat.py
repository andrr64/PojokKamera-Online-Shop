from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.alamat import Alamat
from app.schemas.alamat import AlamatCreate, AlamatUpdate


class AlamatCRUD:
    @staticmethod
    def create(db: Session, alamat_data: AlamatCreate, pengguna_id: int) -> Alamat:
        db_alamat = Alamat(
            pengguna_id=pengguna_id,
            label=alamat_data.label,
            jalan=alamat_data.jalan,
            kota=alamat_data.kota,
            provinsi=alamat_data.provinsi,
            kode_pos=alamat_data.kode_pos,
            negara=alamat_data.negara or "Indonesia"
        )
        db.add(db_alamat)
        db.commit()
        db.refresh(db_alamat)
        return db_alamat

    @staticmethod
    def get_by_id(db: Session, alamat_id: int) -> Optional[Alamat]:
        return db.query(Alamat).filter(Alamat.alamat_id == alamat_id).first()

    @staticmethod
    def get_by_pengguna(db: Session, pengguna_id: int) -> List[Alamat]:
        return db.query(Alamat).filter(Alamat.pengguna_id == pengguna_id).all()

    @staticmethod
    def update(db: Session, alamat: Alamat, update_data: AlamatUpdate) -> Alamat:
        for field, value in update_data.dict(exclude_unset=True).items():
            setattr(alamat, field, value)
        db.commit()
        db.refresh(alamat)
        return alamat

    @staticmethod
    def delete(db: Session, alamat: Alamat) -> None:
        db.delete(alamat)
        db.commit()
