from pydantic import BaseModel, EmailStr, Field
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

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str  

class UserRead(UserBase):
    pengguna_id: int
    peran: str
    dibuat_pada: datetime
    diperbarui_pada: datetime

    class Config:
        from_attributes = True

class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    
class UserLogin(BaseModel):
    email: EmailStr
    password: str
    
class UserRegister(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=8)
    
class AdminLogin(BaseModel):
    username: str
    password: str
    