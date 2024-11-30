from pydantic import BaseModel, EmailStr


class ModeratorBase(BaseModel):
    username: str
    email: EmailStr


class ModeratorUpdate(BaseModel):
    email: EmailStr
