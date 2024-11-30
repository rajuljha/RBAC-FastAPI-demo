from fastapi import APIRouter, Depends, HTTPException
from auth.auth_utils import get_current_user, require_self_or_admin
from auth.model_moderators import ModeratorBase, ModeratorUpdate
from db.users_db import users_db

moderator_router = APIRouter()


@moderator_router.get("/{username}", response_model=ModeratorBase, summary="Get moderator details")
async def get_moderator(username: str, user: dict = Depends(require_self_or_admin)):
    """
    Retrieve moderator details.
    - Self: Moderators can fetch their own data.
    - Admin: Admins can fetch any moderator's data.
    """
    moderator = users_db.get(username)
    if not moderator or moderator["role"] != "moderator":
        raise HTTPException(status_code=404, detail="Moderator not found")
    return {"username": moderator["username"], "email": moderator["email"]}


@moderator_router.put("/{username}", summary="Update moderator details")
async def update_moderator(username: str, update: ModeratorUpdate,
                        user: dict = Depends(require_self_or_admin)):
    """
    Update moderator details.
    - Self: Moderators can update their own data.
    - Admin: Admins can update any moderator's data.
    """
    moderator = users_db.get(username)
    if not moderator or moderator["role"] != "moderator":
        raise HTTPException(status_code=404, detail="Moderator not found")
    moderator["email"] = update.email
    return {"message": f"Moderator {username} updated successfully"}
