# app/main.py
from fastapi import FastAPI, Request
from app.api.v1.user import router as users_router
from fastapi.middleware.cors import CORSMiddleware
from app.core.database import Base, engine
from fastapi.exceptions import RequestValidationError
from app.models import *
from fastapi.responses import JSONResponse
from app.schemas.response import ResponseModel
from app.api.v1 import produk as produk_router

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


app.include_router(users_router, prefix="/api/v1/user", tags=["user"])
app.include_router(produk_router.router, prefix="/api/v1/produk", tags=["produk"])

print("Backend on localhost:8000\n")

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}