# app/middleware/auth.py
from fastapi import Request, status
from fastapi.responses import JSONResponse
from app.utils.jwt import verify_token

async def auth_middleware(request: Request, call_next):
    # Ambil token dari Cookie
    token = request.cookies.get("access_token")

    # Kalau tidak ada di Cookie, coba dari Header Authorization
    if not token:
        auth_header = request.headers.get("Authorization")
        if auth_header and auth_header.startswith("Bearer "):
            token = auth_header.split(" ")[1]

    if not token:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={"detail": "Token tidak ditemukan"}
        )

    # Verifikasi token
    payload = verify_token(token)
    if not payload:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={"detail": "Token tidak valid atau sudah expired"}
        )

    # Simpan user info ke request.state biar bisa dipakai di endpoint
    request.state.user = payload

    # Lanjut ke request berikutnya
    response = await call_next(request)
    return response
