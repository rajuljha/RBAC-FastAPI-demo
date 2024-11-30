from pydantic import BaseModel, EmailStr


class AdminBase(BaseModel):
    username: str
    email: EmailStr


class AdminUpdate(BaseModel):
    email: EmailStr
