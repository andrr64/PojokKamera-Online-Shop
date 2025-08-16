from app.schemas.kategori import KategoriCreate, KategoriResponse
from sqlalchemy.orm import Session
from app.crud.kategori import KategoriCRUD

class KategoriService:
    @staticmethod
    def create_kategori(kategori: KategoriCreate, db: Session) -> KategoriResponse:
        return KategoriResponse.model_validate(
            KategoriCRUD.create_kategori(kategori, db) 
        )
    
    @staticmethod
    def get_all_kategori(db: Session) -> list[KategoriResponse]:
        kategori_list = KategoriCRUD.get_all_kategori(db)
        return [KategoriResponse.model_validate(k) for k in kategori_list]
    
    
    @staticmethod
    def delete_kategori(kategori_id: int, db: Session) -> None:
        KategoriCRUD.delete_kategori(kategori_id, db)