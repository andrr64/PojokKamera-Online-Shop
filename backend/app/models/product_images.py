from app.core.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class ProductImages(Base):
    __tablename__ = "product_images"
    image_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    produk_id = Column(Integer, ForeignKey("produk.produk_id"), nullable=False)
    indeks = Column(Integer, nullable=False)    
    url = Column(String, nullable=False)
    public_id = Column(String, nullable=False)

    # Relasi
    produk = relationship("Produk", back_populates="images")