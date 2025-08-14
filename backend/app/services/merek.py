# app/services/merek.py
from app.utils.upload import upload_logo_merek
from app.crud.merek import MerekCRUD
from sqlalchemy.orm import Session
from app.schemas.merek import MerekCreate   

class MerekService:
    @staticmethod
    def tambah_merek(nama: str, deskripsi: str, logo_file, db: Session):
        logo_url = upload_logo_merek(logo_file)
        
        data = MerekCreate(
            nama=nama,
            deskripsi=deskripsi,
            logo=logo_url
        )
        
        return MerekCRUD.create_merek(db=db, merek_data=data)

    @staticmethod
    def update_merek(merek_id: int, nama: str | None = None, deskripsi: str | None = None, logo_file=None, db: Session = None):
        # Upload logo jika ada
        logo_url = upload_logo_merek(logo_file) if logo_file else None

        # Buat data schema untuk update
        data = MerekCreate(
            nama=nama,
            deskripsi=deskripsi,
            logo=logo_url
        )

        # Panggil CRUD
        return MerekCRUD.update_merek(db=db, merek_id=merek_id, merek_data=data)
