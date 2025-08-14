# app/schemas/merek.py
from pydantic import BaseModel

class MerekCreate(BaseModel):
    nama: str
    deskripsi: str
    logo: str 
    
    class Config:
        orm_mode = True