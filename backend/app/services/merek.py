# app/services/merek.py
from app.utils.upload import upload_logo_merek
from app.crud.merek import create_merek 
from sqlalchemy.orm import Session
from app.schemas.merek import MerekCreate   

def tambah_merek(nama: str, deskripsi: str | None, logo_file, db: Session):
    logo_url = upload_logo_merek(logo_file)
    data = MerekCreate(
        nama=nama,
        deskripsi=deskripsi,
        logo=logo_url
    )
    return create_merek(db=db, merek_data=data)
