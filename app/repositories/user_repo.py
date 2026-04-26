from app.models.user import User


class UserRepository:
    def __init__(self, db):
        self.db = db

    def get_by_email(self, email: str):
        return self.db.query(User).filter(User.email == email).first()

    def create_user(self, email: str, password: str):
        user = User(email=email, password=password)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
