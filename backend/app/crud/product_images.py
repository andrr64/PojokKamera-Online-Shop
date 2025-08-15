from sqlalchemy.orm import Session
from app.models.product_images import ProductImages

class ProductImagesCRUD:
    @staticmethod
    def create(db: Session, product_id: int, image_path: str, public_id: str, indeks: int) -> ProductImages:
        new_image = ProductImages(
            produk_id=product_id, 
            indeks=indeks,
            url=image_path, 
            public_id=public_id,
        )
        db.add(new_image)
        db.commit()
        db.refresh(new_image)
        return new_image