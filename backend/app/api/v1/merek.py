# app/api/v1/merek.py
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.response import ResponseModel
from app.services.merek import tambah_merek
from fastapi import APIRouter, UploadFile, File, Form, Depends
router = APIRouter()

@router.post("/", response_model=ResponseModel, status_code=status.HTTP_201_CREATED)
def create_merek(
    nama: str = Form(...),
    deskripsi: str = Form(None),
    logo_file: UploadFile = File(None),
    db: Session = Depends(get_db)
):
    try:
        tambah_merek(nama, deskripsi, logo_file, db)
        return ResponseModel(
            message="Merek berhasil ditambahkan"
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Terjadi kesalahan internal"
        )
