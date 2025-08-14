# app/services/produk.py
from sqlalchemy.orm import Session
from app.schemas.produk import ProdukCreate
from app.crud.produk import create_produk

def tambah_produk(db: Session, produk_data: ProdukCreate):
    # Bisa tambahkan validasi tambahan di sini, contoh:
    if produk_data.stok < 0:
        raise ValueError("Stok tidak boleh negatif")
    return create_produk(db, produk_data)
