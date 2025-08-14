from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserRole:
    USER = "user"
    ADMIN = "admin"
    
    @staticmethod
    def isAdmin(role: str) -> bool:
        return role == UserRole.ADMIN
    
    @staticmethod
    def isUser(role: str) -> bool:
        return role == UserRole.USER

# Schema dasar untuk membaca data user
class UserBase(BaseModel):
    username: str
    email: EmailStr

# Schema untuk input saat create
class UserCreate(UserBase):
    password: str  

# Schema untuk output/read
class UserRead(UserBase):
    pengguna_id: int
    peran: str
    dibuat_pada: datetime
    diperbarui_pada: datetime

    class Config:
        orm_mode = True

# Schema untuk update user
class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    
class UserLogin(BaseModel):
    email: EmailStr
    password: str