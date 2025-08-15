# app/api/v1/produk.py
from fastapi import APIRouter, Depends, Query, status, HTTPException, Form, UploadFile, File
from sqlalchemy.orm import Session
from app.schemas.response import ResponseModel
from app.core.database import get_db
from app.services.produk import ProdukService
from typing import List
from app.exceptions import NotFoundException, DuplicateException
from app.schemas.produk import ProdukCreateResponse, ProductCardResponse

import logging
router = APIRouter()

@router.get("/get-cards", response_model=ResponseModel, status_code=status.HTTP_200_OK)
def get_product_card(
    keyword: str | None = Query(None, description="Filter berdasarkan keyword nama/deskripsi"),
    merek_id: int | None = Query(None, description="Filter berdasarkan ID merek"),
    db: Session = Depends(get_db)
):
    try:
        data = ProdukService.get_product_card(db=db, keyword=keyword, merek_id=merek_id)
        return ResponseModel(
            detail="Product Cards Data",
            data=data
        )
    except Exception as e:
        print(str(e))
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Terjadi kesalahan internal"
        )

@router.post("/create", response_model=ResponseModel, status_code=status.HTTP_201_CREATED)
def create_product(
    nama: str = Form(...),
    deskripsi: str | None = Form(None),
    harga: float = Form(...),
    stok: int = Form(...),
    kategori_id: int | None = Form(None),
    merek_id: int | None = Form(None),
    images: List[UploadFile] | None = File(None, description="List of product images"),
    db: Session = Depends(get_db)
):
    logging.info(f"Received data: nama={nama}, deskripsi={deskripsi}, harga={harga}, stok={stok}, kategori_id={kategori_id}, merek_id={merek_id}, images={len(images)}")
    try:
        data = ProdukService.create_product(
            db=db,
            nama=nama,
            deskripsi=deskripsi,
            harga=harga,
            stok=stok,
            kategori_id=kategori_id,
            merek_id=merek_id,
            images=images
        )
        return ResponseModel(
            detail="Produk berhasil dibuat",
            data= data
        )
    except NotFoundException as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )
    except DuplicateException as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except Exception as e:
        print(f"Error creating product: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Terjadi kesalahan internal"
        )
