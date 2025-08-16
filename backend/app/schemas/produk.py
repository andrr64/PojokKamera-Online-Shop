# app/schemas/produk.py
from pydantic import BaseModel, condecimal
from typing import Optional, List

class ProdukCreate(BaseModel):
    nama: str
    deskripsi: Optional[str] = None
    harga: float
    stok: int
    kategori_id: Optional[int] = None
    merek_id: Optional[int] = None

    class Config:
        from_attributes = True  # agar bisa digunakan dengan ORM (Produk)


# Response
class ProductCardResponse(BaseModel):
    nama: str
    thumbnail: Optional[str]  # ambil images[0], bisa None kalau ga ada
    deskripsi: Optional[str]
    harga: float
    stok: int
    merek: Optional[str]  

    class Config:
        orm_mode = True

class ProductImageResponse(BaseModel):
    image_id: int
    url: str
    indeks: int

    class Config:
        from_attributes = True  # Ganti dari `orm_mode=True` (untuk Pydantic v2)

class ProdukCreateResponse(BaseModel):
    produk_id: int
    nama: str
    deskripsi: Optional[str] = None
    harga: float
    stok: int
    kategori_id: Optional[int] = None
    merek_id: Optional[int] = None
    images: List[ProductImageResponse] = []

    class Config:
        from_attributes = True