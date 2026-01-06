from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.api.routes_api import router as pet_router
from app.db.database import create_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    create_tables()
    yield
    # Shutdown (optional cleanup)

app = FastAPI(lifespan=lifespan)

app.include_router(pet_router)
