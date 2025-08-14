# app/main.py
from fastapi import FastAPI
from app.api.v1.user import router as users_router
from fastapi.middleware.cors import CORSMiddleware
from app.core.database import Base, engine

# 🔽 Impor model HARUS di sini, sebelum create_all
from app.models.user import User
from app.models.alamat import Alamat
from app.models.merek import Merek
from app.models.kategori import Kategori
from app.models.alamat import Alamat
from app.models.produk import Produk
from app.models.ulasan import Ulasan
from app.models.pesanan import Pesanan
from app.models.item_pesanan import ItemPesanan

# 🔻 Cetak daftar tabel untuk debug
print("\nTabel dalam metadata:")
for table_name in Base.metadata.tables.keys():
    print(f" - {table_name}")
print("\n")

# 🔻 Buat semua tabel
Base.metadata.create_all(bind=engine)
print("✅ Semua tabel berhasil dibuat (atau sudah ada)\n")

app = FastAPI(title="My API", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}