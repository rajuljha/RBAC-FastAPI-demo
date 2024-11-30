# Mock DB for users
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


users_db = {
    "admin1": {
        "username": "admin1",
        "email": "admin1@example.com",
        "password": pwd_context.hash("adminpassword"),
        "role": "admin",
    },
    "moderator1": {
        "username": "moderator1",
        "email": "moderator1@example.com",
        "password": pwd_context.hash("modpassword"),
        "role": "moderator",
    },
    "client1": {
        "username": "client1",
        "email": "client1@example.com",
        "password": pwd_context.hash("clientpassword"),
        "role": "client",
    },
    "admin2": {
        "username": "admin2",
        "email": "admin2@example.com",
        "password": pwd_context.hash("adminpassword2"),
        "role": "admin",
    }
}
