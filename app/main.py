from fastapi import FastAPI
from app.routes.creative_routes import router
from app.database import Base, engine
from app.models.post_model import Post

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router)