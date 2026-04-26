# Auth System

A simple FastAPI authentication API with signup and login endpoints, SQLAlchemy models, database sessions, and password hashing with `bcrypt`.

## Features

- User signup and login endpoints
- Email validation through Pydantic schema rules
- Password hashing with `bcrypt`
- SQLAlchemy-based `User` model
- Database connection configured through environment variables
- Automatic table creation on application startup

## Tech Stack

- FastAPI
- Uvicorn
- SQLAlchemy
- Pydantic
- python-dotenv
- bcrypt
- psycopg2-binary for PostgreSQL connections

## Project Structure

```text
app/
  api/v1/
    endpoints/auth.py     # Auth routes
    router.py             # API router
  core/
    config.py             # Environment configuration
    security.py           # Password hashing and verification
  db/
    base.py               # SQLAlchemy base
    session.py            # Database engine and session
  models/
    user.py               # User table model
  repositories/
    user_repo.py          # Database access layer
  schemas/
    user.py               # Request validation schemas
  services/
    auth_service.py       # Signup and login business logic
main.py                   # FastAPI app entry point
```

## API Flow

### Signup

1. Client sends `email` and `password` to `/api/v1/auth/signup`
2. Request body is validated by `UserCreate`
3. The service checks whether the email already exists
4. The password is hashed with `bcrypt`
5. The new user is stored in the `users` table

### Login

1. Client sends `email` and `password` to `/api/v1/auth/login`
2. The service looks up the user by email
3. The submitted password is compared against the stored hash
4. A success or error response is returned

## Setup

### 1. Create a virtual environment

```powershell
python -m venv myenv
```

### 2. Activate the virtual environment

```powershell
.\\myenv\\Scripts\\Activate.ps1
```

### 3. Install dependencies

```powershell
pip install fastapi uvicorn sqlalchemy python-dotenv bcrypt psycopg2-binary
```

If you are using SQLite instead of PostgreSQL, you can omit `psycopg2-binary` and set a SQLite database URL in `.env`.

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
DATABASE_URL=postgresql://username:password@localhost:5432/auth_system
SECRET_KEY=your_secret_key_here
```

The repository also includes `.env.example` as a reference.

### 5. Run the application

```powershell
uvicorn app.main:app --reload
```

The API will start at:

```text
http://127.0.0.1:8000
```

Interactive docs:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## Endpoints

### `POST /api/v1/auth/signup`

Request body:

```json
{
  "email": "elango@gmail.com",
  "password": "elango123"
}
```

Response:

```json
{
  "message": "User created successfully"
}
```

### `POST /api/v1/auth/login`

Request body:

```json
{
  "email": "elango@gmail.com",
  "password": "elango123"
}
```

Response:

```json
{
  "message": "Login successful"
}
```

## Implementation Notes

- `app/main.py` creates the database tables on startup with `Base.metadata.create_all(bind=engine)`.
- `app/db/session.py` builds the SQLAlchemy engine and session factory.
- `app/repositories/user_repo.py` contains the database operations for reading and writing users.
- `app/services/auth_service.py` contains the signup and login business logic.
- `app/core/security.py` handles password hashing and verification with `bcrypt`.

## Future Improvements

- Add separate request schemas for signup and login
- Add JWT token generation after login
- Add Alembic migrations instead of relying on `create_all`
- Add password strength rules
- Add tests for auth, repository, and security layers