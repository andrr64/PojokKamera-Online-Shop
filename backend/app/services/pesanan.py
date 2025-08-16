#app/service/pesanan.py
from sqlalchemy.orm import Session
from typing import List, Dict, Any, Optional
from app.models.pesanan import Pesanan
from app.models.item_pesanan import ItemPesanan
from app.repositories.pesanan import PesananRepository
from app.crud.produk import ProdukCRUD
from typing import List
from app.models.pesanan import Pesanan
from app.models.item_pesanan import ItemPesanan
from app.models.produk import Produk
from app.repositories.pesanan import PesananRepository
from app.crud.produk import ProdukCRUD
from app.schemas.pesanan import PesananCreate


class PesananService:
    @staticmethod
    def create_pesanan(
        db: Session,
        pesanan_data: PesananCreate
    ) -> Pesanan:
        try:
            # ambil data dari schema
            pengguna_id = pesanan_data.pengguna_id
            alamat_id = pesanan_data.alamat_id
            produk_ids = pesanan_data.produk_ids
            produk_stocks = pesanan_data.produk_stocks

            # 1. cek stok
            stok_ok = ProdukCRUD.is_stok_ok(db, produk_ids, produk_stocks)
            if not stok_ok:
                raise ValueError("Stok tidak mencukupi untuk beberapa produk")

            # 2. hitung total harga
            total_harga = 0
            for produk_id, jumlah in zip(produk_ids, produk_stocks):
                produk = db.query(Produk).filter(Produk.produk_id == produk_id).first()
                if not produk:
                    raise ValueError(f"Produk {produk_id} tidak ditemukan")
                total_harga += produk.harga * jumlah

            # 3. buat pesanan
            pesanan = Pesanan(
                pengguna_id=pengguna_id,
                alamat_id=alamat_id,
                status="pending",
                total_harga=total_harga,
            )
            PesananRepository.create_pesanan(db, pesanan)

            # 4. item pesanan & kurangi stok
            for produk_id, jumlah in zip(produk_ids, produk_stocks):
                produk = db.query(Produk).filter(Produk.produk_id == produk_id).first()
                if not produk or produk.stok < jumlah:
                    raise ValueError(f"Stok produk {produk_id} tidak cukup")

                item = ItemPesanan(
                    pesanan_id=pesanan.pesanan_id,
                    produk_id=produk_id,
                    jumlah=jumlah,
                    harga=produk.harga,
                )
                PesananRepository.create_item_pesanan(db, item)

                produk.stok -= jumlah
                db.add(produk)

            db.commit()
            db.refresh(pesanan)
            return pesanan

        except Exception as e:
            db.rollback()
            raise e

    @staticmethod
    def get_pesanan_by_id(db: Session, pesanan_id: int) -> Pesanan:
        """
        Ambil detail pesanan berdasarkan ID
        """
        return PesananRepository.get_pesanan_by_id(db, pesanan_id)

    @staticmethod
    def get_all_pesanan(db: Session, user_id) -> List:
        return PesananRepository.get_all_pesanan_by_user(db, user_id)

    @staticmethod
    def update_status(db: Session, pesanan_id: int, status: str) -> Pesanan:
        """
        Update status pesanan (pending → dibayar → dikirim → selesai → dibatalkan)
        """
        return PesananRepository.update_pesanan_status(db, pesanan_id, status)

    @staticmethod
    def delete_pesanan(db: Session, pesanan_id: int) -> Pesanan:
        """
        Hapus pesanan
        """
        return PesananRepository.delete_pesanan(db, pesanan_id)

    @staticmethod
    def get_items_by_pesanan(db: Session, pesanan_id: int) -> List[ItemPesanan]:
        """
        Ambil daftar item berdasarkan pesanan
        """
        return PesananRepository.get_items_by_pesanan(db, pesanan_id)
