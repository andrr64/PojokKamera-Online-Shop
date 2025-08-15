from pydantic import BaseModel, Field
from typing import Optional

class KategoriCreate(BaseModel):
    nama: str = Field(..., max_length=50)
    deskripsi: Optional[str] = None  # nullable string
    
    class Config:
        orm_mode = True
