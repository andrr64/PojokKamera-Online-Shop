# app/schemas/merek.py
from pydantic import BaseModel

class MerekCreate(BaseModel):
    nama: str | None
    deskripsi: str |  None
    logo: str | None

class MerekRead(BaseModel):
    nama: str
    deskripsi: str
    logo: str

    model_config = {
        "from_attributes": True,
    }