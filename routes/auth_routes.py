from fastapi import APIRouter, HTTPException, Depends, status
from pydantic import BaseModel
from datetime import timedelta
from auth.auth_utils import create_access_token, verify_password, get_password_hash
from db.users_db import users_db

auth_router = APIRouter()


class LoginRequest(BaseModel):
    username: str
    password: str


class RegisterRequest(BaseModel):
    username: str
    email: str
    password: str
    role: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str


@auth_router.post("/register", summary="Register a new user")
async def register_user(request: RegisterRequest):
    if request.username in users_db:
        raise HTTPException(status_code=400, detail="Username already exists")

    hashed_password = get_password_hash(request.password)
    users_db[request.username] = {
        "username": request.username,
        "email": request.email,
        "password": hashed_password,
        "role": request.role,
    }
    return {"message": "User registered successfully"}


@auth_router.post("/token", response_model=TokenResponse, summary="Log in to get an access token")
async def login_user(request: LoginRequest):
    user = users_db.get(request.username)
    if not user or not verify_password(request.password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid username or password")

    access_token = create_access_token(data={"sub": user["username"]}, expires_delta=timedelta(minutes=30))
    return {"access_token": access_token, "token_type": "bearer"}
