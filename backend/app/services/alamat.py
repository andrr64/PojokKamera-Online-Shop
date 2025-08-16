from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.schemas.alamat import AlamatCreate, AlamatUpdate, AlamatResponse
from app.crud.alamat import AlamatCRUD
from app.crud.user import UserCRUD  # asumsi ada UserCRUD
from app.models.alamat import Alamat


class AlamatService:
    @staticmethod
    def tambah_alamat(db: Session, user: dict, alamat_data: AlamatCreate) -> AlamatResponse:
        user_email = user.get("sub")

        pengguna = UserCRUD.get_by_email(db, user_email)
        if not pengguna:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Pengguna tidak ditemukan"
            )

        alamat = AlamatCRUD.create(db, alamat_data, pengguna_id=pengguna.pengguna_id)
        return AlamatResponse.model_validate(alamat)

    @staticmethod
    def get_daftar_alamat(db: Session, user_id: str):
        pengguna = UserCRUD.get_by_id(db, user_id)
        if not pengguna:
            raise HTTPException(status_code=404, detail="Pengguna tidak ditemukan")

        alamat_list = AlamatCRUD.get_by_pengguna(db, pengguna_id=pengguna.pengguna_id)
        return [AlamatResponse.model_validate(a) for a in alamat_list]

    @staticmethod
    def update_alamat(db: Session, user: dict, alamat_id: int, update_data: AlamatUpdate):
        user_email = user.get("sub")
        pengguna = UserCRUD.get_by_email(db, user_email)
        if not pengguna:
            raise HTTPException(status_code=404, detail="Pengguna tidak ditemukan")

        alamat = AlamatCRUD.get_by_id(db, alamat_id)
        if not alamat or alamat.pengguna_id != pengguna.pengguna_id:
            raise HTTPException(status_code=404, detail="Alamat tidak ditemukan")

        updated = AlamatCRUD.update(db, alamat, update_data)
        return AlamatResponse.model_validate(updated)

    @staticmethod
    def hapus_alamat(db: Session, user: dict, alamat_id: int):
        user_email = user.get("sub")
        pengguna = UserCRUD.get_by_email(db, user_email)
        if not pengguna:
            raise HTTPException(status_code=404, detail="Pengguna tidak ditemukan")

        alamat = AlamatCRUD.get_by_id(db, alamat_id)
        if not alamat or alamat.pengguna_id != pengguna.pengguna_id:
            raise HTTPException(status_code=404, detail="Alamat tidak ditemukan")

        AlamatCRUD.delete(db, alamat)
        return {"message": "Alamat berhasil dihapus"}
