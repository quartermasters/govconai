from fastapi import FastAPI
from .db.database import engine, Base
from .api import v1
from .core.config import settings
from celery import Celery

app = FastAPI(title=settings.PROJECT_NAME)

# Celery configuration
celery_app = Celery(
    "govconai_scraper",
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL
)
celery_app.conf.update(app.extra)

@app.on_event("startup")
async def startup_event():
    Base.metadata.create_all(bind=engine)

app.include_router(v1.router, prefix="/api/v1")

@app.get("/")
async def read_root():
    return {"message": "Welcome to GovconAI Scraper Module"}