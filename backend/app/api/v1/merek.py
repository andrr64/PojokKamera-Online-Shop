# app/api/v1/merek.py
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.response import ResponseModel
from app.services.merek import tambah_merek
from fastapi import APIRouter, UploadFile, File, Form, Depends
router = APIRouter()

@router.post("/create", response_model=ResponseModel, status_code=status.HTTP_201_CREATED)
def create_merek(
    nama: str = Form(...),
    deskripsi: str = Form(...),
    logo_file: UploadFile = File(None),
    db: Session = Depends(get_db)
):
    try:
        tambah_merek(nama=nama, deskripsi=deskripsi, logo_file=logo_file, db=db)
        return ResponseModel(
            detail="Merek berhasil ditambahkan"
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except Exception as e:
        print(str(e))
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Terjadi kesalahan internal"
        )
