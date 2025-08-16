from pydantic import BaseModel
from typing import List
from decimal import Decimal

class PesananCreate(BaseModel):
    pengguna_id: int | None = None
    alamat_id: int
    produk_ids: List
    produk_stocks: List[int]
    
    

class ItemPesananCreate(BaseModel):
    produk_id: int
    quantity: int

class PesananCreate(BaseModel):
    alamat_id: int
    items: List[ItemPesananCreate]
    total_harga: Decimal
