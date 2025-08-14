# app/schemas/merek.py
from pydantic import BaseModel

class MerekCreate(BaseModel):
    nama: str | None
    deskripsi: str |  None
    logo: str | None
    
    class Config:
        orm_mode = True