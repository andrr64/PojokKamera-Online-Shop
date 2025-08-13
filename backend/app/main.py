# app/main.py
from fastapi import FastAPI
from app.api.v1.user import router as users_router
from app.core.database import Base, engine
from fastapi.middleware.cors import CORSMiddleware

# Buat tabel (hanya untuk dev, produksi gunakan Alembic)
# Base.metadata.create_all(bind=engine)


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