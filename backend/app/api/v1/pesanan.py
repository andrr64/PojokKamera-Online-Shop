from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.schemas.pesanan import PesananCreate
from app.core.database import get_db
from app.dependencies.auth import get_current_user
from app.services.pesanan import PesananService
from app.enum.status_pesanan import StatusPesananEnum

router = APIRouter()

@router.post("/add")
def buat_psanan(
    pesanan: PesananCreate, 
    db: Session = Depends(get_db), 
    user = Depends(get_current_user)
):
    try:
        pesanan.pengguna_id = user.get("sub")
        result = PesananService.create_pesanan(
            db, pesanan
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {"message": "Pesanan berhasil dibuat"}

@router.get("/get-all")
def get_semua_pesanan(
    db: Session = Depends(get_db), 
    user = Depends(get_current_user)
):
    try:
        result = PesananService.get_all_pesanan(db, user.get("sub"))
        return {"pesanan": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/get-all-admin")
def get_semua_pesanan_admin(
    db: Session = Depends(get_db),
    status: StatusPesananEnum | None = Query(None, description="Filter status pesanan")
):
    """
    Ambil semua pesanan untuk admin, bisa difilter berdasarkan status_pesanan.
    """
    try:
        result = PesananService.get_all_pesanan_admin(db, status)
        return {"pesanan": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))