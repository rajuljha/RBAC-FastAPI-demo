from fastapi import FastAPI
from routes.admin_routes import admin_router
from routes.moderator_routes import moderator_router
from routes.client_routes import client_router
from routes.auth_routes import auth_router

app = FastAPI(
    title="RBAC Application",
    description="Role-Based Access Control with FastAPI",
    version="1.0.0"
)

# Register Routers
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(admin_router, prefix="/admin", tags=["Admin"])
app.include_router(moderator_router, prefix="/moderator", tags=["Moderator"])
app.include_router(client_router, prefix="/client", tags=["Client"])


@app.get("/", summary="Welcome Endpoint")
async def root():
    return {"message": "Welcome to the RBAC application!"}
