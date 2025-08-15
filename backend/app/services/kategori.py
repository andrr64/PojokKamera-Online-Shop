from app.schemas.kategori import KategoriCreate
from sqlalchemy.orm import Session
from app.crud.kategori import KategoriCRUD

class KategoriService:
    
    @staticmethod
    def create_kategori(kategori: KategoriCreate, db: Session):
        result = KategoriCRUD.create_kategori(kategori, db) 
        return result