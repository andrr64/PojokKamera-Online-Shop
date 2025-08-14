# app/services/merek.py
from app.crud.merek import MerekCRUD
from sqlalchemy.orm import Session
from app.schemas.merek import MerekCreate
from app.services.upload_image import upload_image, hapus_image
from datetime import datetime
from typing import List

class MerekService:
    
    @staticmethod
    def tambah_merek(nama: str, deskripsi: str, logo_file, db: Session):
        logo_url = None
        
        if logo_file:
            public_id = f"{nama.replace(' ', '_').lower()}_{datetime.now().isoformat().replace(' ', '_')}"
            logo_url = upload_image(
                file=logo_file.file,
                public_id=public_id,
                folder="merek"
            )
        else:
            raise ValueError("Logo file tidak boleh kosong")
        
        data = MerekCreate(
            nama=nama,
            deskripsi=deskripsi,
            logo=logo_url
        )
        
        try:
            return MerekCRUD.create_merek(db=db, merek_data=data)
        except Exception as e:
            if (logo_url and public_id):
                hapus_image(public_id) 
            raise ValueError(f"Terjadi kesalahan saat menambahkan merek: {str(e)}")

    @staticmethod
    def update_merek(merek_id: int, nama: str | None = None, deskripsi: str | None = None, logo_file=None, db: Session = None):
        # Ambil data lama
        db_merek = MerekCRUD.get_merek_by_id(db, merek_id)
        if not db_merek:
            raise ValueError("Merek tidak ditemukan")

        # Tentukan nilai baru, pakai data lama jika kosong
        new_nama = nama if nama else db_merek.nama
        new_deskripsi = deskripsi if deskripsi else db_merek.deskripsi
        new_logo_url = db_merek.logo
        new_public_id = None

        # Upload logo baru jika ada
        if logo_file:
            new_public_id = f"merek/{new_nama.replace(' ', '_').lower()}"
            try:
                new_logo_url, uploaded_public_id = upload_image(
                    file=logo_file,
                    public_id=new_public_id,
                    folder="merek"
                )
                new_public_id = uploaded_public_id
            except Exception as e:
                raise ValueError(f"Gagal upload logo baru: {str(e)}")

        # Buat schema untuk update
        data = MerekCreate(
            nama=new_nama,
            deskripsi=new_deskripsi,
            logo=new_logo_url
        )

        try:
            # Update di database
            updated_merek = MerekCRUD.update_merek(db=db, merek_id=merek_id, merek_data=data)

            # Jika ada logo baru dan ada logo lama, hapus logo lama
            if logo_file and db_merek.logo:
                old_public_id = db_merek.logo.split("/")[-1].split(".")[0]  # Ambil public_id dari URL
                hapus_image(old_public_id)

            return updated_merek
        except Exception as e:
            # Jika gagal, hapus logo baru agar tidak menumpuk
            if logo_file and new_public_id:
                hapus_image(new_public_id)
            raise ValueError(f"Terjadi kesalahan saat update merek: {str(e)}")

    @staticmethod
    def read_all_merek(db: Session):
        return MerekCRUD.get_all_merek(db)
    
    @staticmethod
    def read_merek_by_id(db: Session, merek_id: int):
        db_merek = MerekCRUD.get_merek_by_id(db, merek_id)
        if not db_merek:
            raise ValueError("Merek tidak ditemukan")
        return db_merek