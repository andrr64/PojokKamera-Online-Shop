# app/api/v1/produk.py
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.schemas.produk import ProdukCreate
from app.schemas.response import ResponseModel
from app.core.database import get_db
from app.services.produk import tambah_produk

router = APIRouter()

@router.post("/", response_model=ResponseModel, status_code=status.HTTP_201_CREATED)
def create_produk(body: ProdukCreate, db: Session = Depends(get_db)):
    try:
        produk = tambah_produk(db, body)
        return ResponseModel(
            message="Produk berhasil ditambahkan",
            data={produk}
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Terjadi kesalahan internal"
        )
