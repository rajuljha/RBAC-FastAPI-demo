from pydantic import BaseModel, EmailStr


class ClientBase(BaseModel):
    username: str
    email: EmailStr


class ClientUpdate(BaseModel):
    email: EmailStr
