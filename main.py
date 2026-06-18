from fastapi import FastAPI
from app.routers.user import router as user_router
from app.database import Base, engine
from app.models.user import User
from app.models.post import Post
from app.models.category import Category

app = FastAPI()

app.include_router(user_router)

Base.metadata.create_all(engine)

