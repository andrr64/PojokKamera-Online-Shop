from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.kategori import KategoriCreate
from app.services.kategori import KategoriService
from app.schemas.response import ResponseModel
from app.exceptions import DuplicateException, NotFoundException

router = APIRouter()

@router.post('/create', status_code= status.HTTP_201_CREATED, response_model=ResponseModel)
def create_kategori(kategori: KategoriCreate, db: Session = Depends(get_db)):
    try:
        return ResponseModel(
            detail="Kategori berhasil dibuat",
            data= KategoriService.create_kategori(kategori, db)
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

@router.get('/get-all', response_model=ResponseModel)
def get_all_kategori(db: Session = Depends(get_db)):
    try:
        kategori_list = KategoriService.get_all_kategori(db)
        return ResponseModel(
            detail="Berhasil mendapatkan semua kategori",
            data=kategori_list
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        ) from e
        
@router.delete("/delete/{kategori_id}", response_model=ResponseModel)
def delete_kategori(kategori_id: int, db: Session = Depends(get_db)): 
    try:
        KategoriService.delete_kategori(kategori_id, db)
        return ResponseModel(
            detail="Kategori berhasil dihapus",
        )
    except NotFoundException as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        ) from e
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        ) from e