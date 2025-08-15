from sqlalchemy.orm import Session
from typing import Optional, List
from app.schemas.produk import ProductCardResponse, ProdukCreateResponse
from app.crud.produk import ProdukCRUD
from app.services.upload_image import upload_image
from app.schemas.produk import ProdukCreate
from app.crud.product_images import ProductImagesCRUD

class ProdukService:
    @staticmethod
    def get_product_card(
        db: Session,
        keyword: Optional[str] = None,
        merek_id: Optional[int] = None
    ) -> List[ProductCardResponse]:
        data = ProdukCRUD.read_produk(db, keyword, merek_id)
        cards = []
        for p in data:
            #  TODO: services.ProductServices.get_product_card handle case where images is empty
            thumbnail_url = p.images[0].url if p.images else None
            cards.append(ProductCardResponse(
                nama=p.nama,
                thumbnail=thumbnail_url,
                deskripsi=p.deskripsi,
                harga=float(p.harga),
                stok=p.stok,
                merek=p.merek.nama if p.merek else None
            ))
        return cards
    
    @staticmethod
    def create_product(
        db: Session,
        nama: str,
        deskripsi: str,
        harga: float,
        stok: int,
        kategori_id: int,
        merek_id: int,
        images: List
    ) -> ProdukCreateResponse:
        # buat produk baru
        try:
            produk_data = ProdukCreate(
                nama=nama,
                deskripsi=deskripsi,
                harga=harga,
                stok=stok,
                kategori_id=kategori_id,
                merek_id=merek_id
            )
            produk = ProdukCRUD.create_produk(db, produk_data)
            
            failed_images_ids = []
            
            for idx, img_file in enumerate(images):
                try:
                    public_id = f"produk/{nama.replace(' ', '_').lower()}_{img_file.filename}"
                    img_url = upload_image(file=img_file.file, public_id=public_id, folder="produk")
                    x = ProductImagesCRUD.create(
                        db=db,
                        product_id=produk.produk_id,
                        indeks=idx,
                        image_path=img_url,
                        public_id=public_id
                    )
                except Exception as e:
                    print(f"Failed to upload image {img_file.filename}: {e}")
                    failed_images_ids.append(idx)
            db.commit()
            db.refresh(produk)
            return ProdukCreateResponse.model_validate(produk)
        except Exception as e:
            print(f"Error creating product: {e}")
            raise e