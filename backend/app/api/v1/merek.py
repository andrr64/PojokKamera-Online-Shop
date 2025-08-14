# app/api/v1/merek.py
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.response import ResponseModel
from app.services.merek import MerekService
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
        MerekService.tambah_merek(nama=nama, deskripsi=deskripsi, logo_file=logo_file, db=db)
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


@router.put("/update/{merek_id}", response_model=ResponseModel)
def update_merek(
    merek_id: int,
    nama: str | None = Form(None),
    deskripsi: str | None = Form(None),
    logo_file: UploadFile = File(None),
    db: Session = Depends(get_db)
):
    try:
        MerekService.update_merek(
            merek_id=merek_id,
            nama=nama,
            deskripsi=deskripsi,
            logo_file=logo_file,
            db=db
        )
        return ResponseModel(
            detail="Merek berhasil diperbarui"
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )
    except Exception as e:
        print(str(e))
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Terjadi kesalahan internal"
        )
