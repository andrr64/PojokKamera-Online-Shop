# app/main.py
from fastapi import FastAPI, Request
from app.api.v1.user import router as users_router
from app.api.v1.auth import router as auth_router
from fastapi.middleware.cors import CORSMiddleware
from app.core.database import Base, engine
from fastapi.exceptions import RequestValidationError
from app.models import *
from fastapi.responses import JSONResponse
from app.schemas.response import ResponseModel

Base.metadata.create_all(bind=engine)
print("✅ Semua tabel berhasil dibuat (atau sudah ada)\n")

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


app.include_router(auth_router, prefix="/api/v1/auth", tags=["auth"])

print("Backend on localhost:8000\n")

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}