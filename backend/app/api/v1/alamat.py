from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_db
from app.dependencies.auth import get_current_user
from app.services.alamat import AlamatService
from app.schemas.alamat import AlamatCreate, AlamatUpdate, AlamatResponse

router = APIRouter()


# CREATE
@router.post("/add", response_model=AlamatResponse, status_code=status.HTTP_201_CREATED)
def tambah_alamat(
    payload: AlamatCreate,
    db: Session = Depends(get_db),
    user: dict = Depends(get_current_user)
):
    try:
        return AlamatService.tambah_alamat(db, user, payload)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# READ ALL (by user)
@router.get("/get-all", response_model=List[AlamatResponse])
def list_alamat(
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):
    user_id = user.get("sub")
    return AlamatService.get_daftar_alamat(db, user_id)


# READ ONE
@router.get("/{alamat_id}", response_model=AlamatResponse)
def get_alamat(
    alamat_id: int,
    db: Session = Depends(get_db),
    user: dict = Depends(get_current_user)
):
    return AlamatService.get_by_id(db, user, alamat_id)


# UPDATE
@router.put("/{alamat_id}", response_model=AlamatResponse)
def update_alamat(
    alamat_id: int,
    payload: AlamatUpdate,
    db: Session = Depends(get_db),
    user: dict = Depends(get_current_user)
):
    return AlamatService.update_alamat(db, user, alamat_id, payload)


# DELETE
@router.delete("/{alamat_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_alamat(
    alamat_id: int,
    db: Session = Depends(get_db),
    user: dict = Depends(get_current_user)
):
    AlamatService.delete_alamat(db, user, alamat_id)
    return {"message": "Alamat berhasil dihapus"}
