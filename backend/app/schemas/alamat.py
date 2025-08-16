from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class AlamatBase(BaseModel):
    label: str
    jalan: str
    kota: str
    provinsi: str
    kode_pos: str
    negara: Optional[str] = "Indonesia"


class AlamatCreate(AlamatBase):
    pass


class AlamatUpdate(BaseModel):
    label: Optional[str]
    jalan: Optional[str]
    kota: Optional[str]
    provinsi: Optional[str]
    kode_pos: Optional[str]
    negara: Optional[str]


class AlamatResponse(AlamatBase):
    alamat_id: int
    pengguna_id: int
    dibuat_pada: datetime
    diperbarui_pada: datetime

    class Config:
        from_attributes = True
