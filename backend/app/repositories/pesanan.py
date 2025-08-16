from sqlalchemy.orm import Session
from typing import List
from app.models.pesanan import Pesanan
from app.models.item_pesanan import ItemPesanan
from sqlalchemy.orm import joinedload


class PesananRepository:
    # ============ PESANAN ============
    @staticmethod
    def create_pesanan(db: Session, pesanan: Pesanan) -> Pesanan:
        db.add(pesanan)
        db.commit()
        db.refresh(pesanan)
        return pesanan
    
    @staticmethod
    def get_all_pesanan_by_user(db: Session, pengguna_id: int):
        return (
            db.query(Pesanan)
            .options(
                joinedload(Pesanan.item_pesanan),
                joinedload(Pesanan.alamat),
                joinedload(Pesanan.pengguna)
            )
            .filter(Pesanan.pengguna_id == pengguna_id).all()
        )

    @staticmethod
    def get_all_pesanan(db: Session, skip: int = 0, limit: int = 10) -> List[Pesanan]:
        return db.query(Pesanan).offset(skip).limit(limit).all()

    @staticmethod
    def update_pesanan_status(db: Session, pesanan_id: int, status: str) -> Pesanan:
        pesanan = PesananRepository.get_pesanan_by_id(db, pesanan_id)
        pesanan.status = status
        db.commit()
        db.refresh(pesanan)
        return pesanan

    @staticmethod
    def delete_pesanan(db: Session, pesanan_id: int) -> Pesanan:
        pesanan = PesananRepository.get_pesanan_by_id(db, pesanan_id)
        db.delete(pesanan)
        db.commit()
        return pesanan

    # ============ ITEM PESANAN ============
    @staticmethod
    def create_item_pesanan(db: Session, item: ItemPesanan) -> ItemPesanan:
        db.add(item)
        db.commit()
        db.refresh(item)
        return item

    @staticmethod
    def get_items_by_pesanan(db: Session, pesanan_id: int) -> List[ItemPesanan]:
        return db.query(ItemPesanan).filter(ItemPesanan.pesanan_id == pesanan_id).all()
