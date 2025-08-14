# app/services/merek.py
from app.utils.upload import upload_logo_merek
from app.crud.merek import create_merek 
from sqlalchemy.orm import Session

def tambah_merek(nama: str, deskripsi: str | None, logo_file, db: Session):
    logo_url = upload_logo_merek(logo_file)
    return create_merek(db=db, nama=nama, deskripsi=deskripsi, logo_url=logo_url)
