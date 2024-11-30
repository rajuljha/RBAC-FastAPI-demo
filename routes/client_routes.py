from fastapi import APIRouter, Depends, HTTPException
from auth.auth_utils import get_current_user, require_self_or_admin
from auth.model_clients import ClientBase, ClientUpdate
from db.users_db import users_db

client_router = APIRouter()


@client_router.get("/{username}", response_model=ClientBase, summary="Get client details")
async def get_client(username: str, user: dict = Depends(require_self_or_admin)):
    """
    Retrieve client details. 
    - Self: Clients can fetch their own data. 
    - Admin: Admins can fetch any client's data.
    """
    client = users_db.get(username)
    if not client or client["role"] != "client":
        raise HTTPException(status_code=404, detail="Client not found")
    return {"username": client["username"], "email": client["email"]}


@client_router.put("/{username}", summary="Update client details")
async def update_client(username: str, update: ClientUpdate, user: dict = Depends(require_self_or_admin)):
    """
    Update client details.
    - Self: Clients can update their own data.
    - Admin: Admins can update any client's data.
    """
    client = users_db.get(username)
    if not client or client["role"] != "client":
        raise HTTPException(status_code=404, detail="Client not found")
    client["email"] = update.email
    return {"message": f"Client {username} updated successfully"}
