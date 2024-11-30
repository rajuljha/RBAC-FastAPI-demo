# Role Based Access Control (RBAC)

### Directory and File Descriptions

- **auth/**: Contains authentication and authorization utilities and models.
  - `auth_utils.py`: Utility functions for password hashing, token creation, and user verification.
  - `model_admin.py`: Pydantic models for Admin.
  - `model_clients.py`: Pydantic models for Clients.
  - `model_moderators.py`: Pydantic models for Moderators.
  - `models.py`: General models for authentication.

- **db/**: Contains mock database for users.
  - `users_db.py`: Mock database with predefined users.

- **routes/**: Contains route definitions for different user roles.
  - `admin_routes.py`: Routes for Admin operations.
  - `auth_routes.py`: Routes for authentication (login, register).
  - `client_routes.py`: Routes for Client operations.
  - `moderator_routes.py`: Routes for Moderator operations.

- **main.py**: Main entry point of the application. Registers all the routers and starts the FastAPI application.

- **requirements.txt**: Lists all the dependencies required for the project.

- **README.md**: This file.

- **.gitignore**: Specifies files and directories to be ignored by git.

## Roles and Permissions

### Admin
- Can view and update any admin's details.
- Can view and update any moderator's details.
- Can view and update any client's details.

### Moderator
- Can view and update their own details.

### Client
- Can view and update their own details.

## Authentication and Authorization

- **Password Hashing**: Passwords are hashed using bcrypt.
- **Token-Based Authentication**: JWT tokens are used for authentication.
- **Role-Based Access Control**: Access to routes is controlled based on user roles.

## API Endpoints

### Authentication
- **POST /auth/register**: Register a new user.
- **POST /auth/token**: Log in to get an access token.

### Admin
- **GET /admin/{username}**: Get admin details.
- **PUT /admin/{username}**: Update admin details.

### Moderator
- **GET /moderator/{username}**: Get moderator details.
- **PUT /moderator/{username}**: Update moderator details.

### Client
- **GET /client/{username}**: Get client details.
- **PUT /client/{username}**: Update client details.

## Running the Application

1. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

2. Run the FastAPI application:
    ```sh
    uvicorn main:app --reload
    ```

3. Access the API documentation at `http://127.0.0.1:8000/docs`.

4. Test with tools like Postman/Curl.

## License

This project is licensed under the MIT License.