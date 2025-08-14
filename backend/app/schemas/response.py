from typing import Optional, Any
from pydantic import BaseModel

class ResponseModel(BaseModel):
    detail: str
    data: Optional[Any] = None  # bisa dict, list, atau None

    class Config:
        orm_mode = True
        json_encoders = {
            str: lambda v: v,
            int: lambda v: v,
            float: lambda v: v,
            bool: lambda v: v,
        }
