# app/crud/produk.py
from sqlalchemy.orm import Session
from app.models.produk import Produk
from app.schemas.produk import ProdukCreate

def create_produk(db: Session, produk_data: ProdukCreate) -> Produk:
    produk = Produk(**produk_data.model_dump())
    db.add(produk)
    db.commit()
    db.refresh(produk)
    return produk