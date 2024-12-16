from fastapi import FastAPI
import models
from database import engine, get_db
import post
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(post.router)