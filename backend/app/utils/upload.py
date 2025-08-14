# app/utils/upload.py
from typing import Optional

def upload_logo_merek(file) -> Optional[str]:
    """
    Upload file ke cloud storage dan return URL publik.

    Args:
        file (UploadFile): file dari FastAPI

    Returns:
        str | None: URL publik file, atau None kalau file kosong
    """
    if not file:
        return None

    # contoh logika: nanti diganti sesuai cloud provider
    # misal Firebase Storage:
    # 1. buat bucket reference
    # 2. simpan file
    # 3. dapatkan public URL
    #
    # Contoh pseudo:
    #
    # file_content = file.file.read()
    # blob = bucket.blob(file.filename)
    # blob.upload_from_string(file_content, content_type=file.content_type)
    # blob.make_public()
    # return blob.public_url

    # sementara return nama file sebagai placeholder
    return f"https://storage.example.com/{file.filename}"
