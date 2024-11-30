from fastapi import APIRouter, Depends, HTTPException
from auth.auth_utils import require_role
from auth.model_admin import AdminBase, AdminUpdate
from db.users_db import users_db

admin_router = APIRouter()


@admin_router.get("/{username}", response_model=AdminBase, summary="Get admin details")
async def get_admin(username: str, admin_user: dict = Depends(require_role("admin"))):
    """
    Retrieve admin details. Only accessible by other admins.
    """
    admin = users_db.get(username)
    if not admin or admin["role"] != "admin":
        raise HTTPException(status_code=404, detail="Admin not found")
    return {"username": admin["username"], "email": admin["email"]}


@admin_router.put("/{username}", summary="Update admin details")
async def update_admin(username: str, update: AdminUpdate, admin_user: dict = Depends(require_role("admin"))):
    """
    Update admin details. Only other admins can update an admin's data.
    """
    admin = users_db.get(username)
    if not admin or admin["role"] != "admin":
        raise HTTPException(status_code=404, detail="Admin not found")
    if admin["username"] == username:
        raise HTTPException(status_code=401, detail="Admin's can't update their own role!")
    admin["email"] = update.email
    return {"message": f"Admin {username} updated successfully"}
