from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.kategori import KategoriCreate
from app.services.kategori import KategoriService
from app.schemas.response import ResponseModel
from app.exceptions import DuplicateException

router = APIRouter()

@router.post('/create', status_code= status.HTTP_201_CREATED, response_model=ResponseModel)
def create_kategori(kategori: KategoriCreate, db: Session = Depends(get_db)):
    try:
        new_kategori = KategoriService.create_kategori(kategori, db)
        return ResponseModel(
            detail="Kategori berhasil dibuat",
            data=new_kategori
        )
    except DuplicateException as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        ) from e
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        ) from e