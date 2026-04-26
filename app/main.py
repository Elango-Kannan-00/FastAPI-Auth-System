from fastapi import FastAPI
from app.api.v1.router import router
from app.db.base import Base
from app.db.session import engine

app = FastAPI(title="Login/SignUp API")

# Create tables
Base.metadata.create_all(bind=engine)

# To include /api/v1 prefix before the api call
app.include_router(router, prefix="/api/v1")

