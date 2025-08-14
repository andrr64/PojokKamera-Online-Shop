# app/schemas/produk.py
from decimal import Decimal
from pydantic import BaseModel, Field
from typing import Optional

class ProdukCreate(BaseModel):
    nama: str
    deskripsi: Optional[str] = None
    harga: Decimal = Field(..., max_digits=12, decimal_places=2)
    stok: int
    kategori_id: Optional[int] = None
    merek_id: Optional[int] = None

    class Config:
        orm_mode = True