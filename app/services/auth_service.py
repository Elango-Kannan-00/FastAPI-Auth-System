from fastapi import HTTPException
from app.repositories.user_repo import UserRepository
from app.core.security import hash_password, verify_password

class AuthService:
    def __init__(self, db):
        self.repo = UserRepository(db)

    def signup(self, user):
        existing = self.repo.get_by_email(user.email)
        if existing:
            raise HTTPException(status_code=400, detail="User already exists")

        hashed = hash_password(user.password)
        self.repo.create_user(user.email, hashed)

        return {"message": "User created successfully"}

    def login(self, user):
        db_user = self.repo.get_by_email(user.email)

        if not db_user:
            raise HTTPException(status_code=401, detail="Invalid email")

        if not verify_password(user.password, db_user.password):
            raise HTTPException(status_code=401, detail="Invalid password")

        return {"message": "Login successful"}