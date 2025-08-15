# app/main.py
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from app.core.database import Base, engine
from fastapi.exceptions import RequestValidationError
from app.models import *
from fastapi.responses import JSONResponse
from app.schemas.response import ResponseModel


Base.metadata.create_all(bind=engine)
app = FastAPI(title="My API", version="1.0")

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content=ResponseModel(
            detail= "Periksa kembali data yang Anda masukkan",
        ).model_dump()
    )
    
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from app.api.v1 import merek as merek_router
from app.api.v1 import user as users_router
from app.api.v1 import produk as produk_router
from app.api.v1 import kategori as kategori_router

app.include_router(merek_router.router, prefix="/api/v1/merek", tags=["merek"])
app.include_router(users_router.router, prefix="/api/v1/user", tags=["user"])
app.include_router(produk_router.router, prefix="/api/v1/produk", tags=["produk"])
app.include_router(kategori_router.router, prefix="/api/v1/kategori", tags=["kategori"])

print("Backend on localhost:8000\n")

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}