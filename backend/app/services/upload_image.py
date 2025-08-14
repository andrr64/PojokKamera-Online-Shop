import cloudinary
import cloudinary.uploader
from cloudinary.utils import cloudinary_url
from app.core.config import settings

# Configuration       
cloudinary.config( 
    cloud_name = "dxg0ldgnm", 
    api_key = "687682946286642", 
    api_secret = settings.CLOUDINARY_KEY, 
    secure=True
)

def upload_image(file, public_id: str, folder: str = "default") -> str:
    upload_result = cloudinary.uploader.upload(file, folder=folder, public_id=public_id)
    return upload_result["secure_url"]

def hapus_image(public_id: str):
    """
    Hapus image dari Cloudinary berdasarkan public_id
    """
    result = cloudinary.uploader.destroy(public_id)
    return result