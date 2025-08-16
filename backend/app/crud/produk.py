# app/crud/produk.py
from sqlalchemy.orm import Session
from sqlalchemy import or_
from typing import Optional
from app.models.produk import Produk
from sqlalchemy import or_, func
from typing import Optional
from fastapi import HTTPException, status
from app.models.merek import Merek
from app.models.kategori import Kategori
from app.schemas.produk import ProdukCreate
from app.exceptions import NotFoundException, DuplicateException
from typing import List
from sqlalchemy.orm import joinedload

class ProdukCRUD:
    
    @staticmethod
    def create_produk(db: Session, produk_data: ProdukCreate) -> Produk:
        # cek apakah merek_id ada
        merek = db.query(Merek).filter(Merek.merek_id == produk_data.merek_id).first()
        if not merek:
            raise NotFoundException(
               f"Merek dengan id {produk_data.merek_id} tidak ditemukan."
            )
        
        # cek apakah kategori_id ada
        kategori = db.query(Kategori).filter(Kategori.kategori_id == produk_data.kategori_id).first()
        if not kategori:
            raise NotFoundException(
               f"Kategori dengan id {produk_data.kategori_id} tidak ditemukan."
            )
        
        # cek duplikat nama produk dalam merek yang sama (case-insensitive)
        existing = db.query(Produk).filter(
            Produk.merek_id == produk_data.merek_id,
            func.lower(Produk.nama) == produk_data.nama.lower()
        ).first()
        if existing:
            raise DuplicateException(
               f"Produk '{produk_data.nama}' pada merek ini sudah ada."
            )
        
        # buat instance Produk baru
        db_produk = Produk(
            nama=produk_data.nama,
            deskripsi=produk_data.deskripsi,
            harga=produk_data.harga,
            stok=produk_data.stok,
            kategori_id=produk_data.kategori_id,
            merek_id=produk_data.merek_id
        )
        
        db.add(db_produk)
        db.commit()
        db.refresh(db_produk)
        return db_produk

    @staticmethod
    def read_produk(
        db: Session,
        keyword: Optional[str] = None,
        merek_id: Optional[int] = None
    ) -> List[Produk]:
        query = db.query(Produk)

        if merek_id is not None:
            query = query.filter(Produk.merek_id == merek_id)
        if keyword:
            like_pattern = f"%{keyword}%"
            query = query.filter(
                or_(
                    Produk.nama.ilike(like_pattern),
                    Produk.deskripsi.ilike(like_pattern)
                )
            )

        return query.all()

    @staticmethod
    def read_by_id(db: Session, produk_id: int) -> Produk:
        produk = (
            db.query(Produk)
            .options(
                joinedload(Produk.merek), # Pastikan relasi "merek" ada di model
                joinedload(Produk.kategori), # Pastikan relasi "kategori" ada di model
                joinedload(Produk.images)  # Pastikan relasi "images" ada di model
            )
            .filter(Produk.produk_id == produk_id)
            .first()
        )
        if not produk:
            from app.exceptions import NotFoundException
            raise NotFoundException(f"Produk dengan ID {produk_id} tidak ditemukan")
        return produk
