from pydantic import BaseModel
from typing import Optional

class Locations(BaseModel):
    latitude_x1:float
    longitude_y1:float
    latitude_x2:float
    longitude_y2:float

class Token(BaseModel):
    access_token: str
    token_type: str
class TokenData(BaseModel):
    username: str | None = None

class TeacherIN(BaseModel):
    teacher_name:str
    id:str
    student_id:str

    
class AdminBase(BaseModel):
    username: str
    password: str

class LoginData(AdminBase):
    pass