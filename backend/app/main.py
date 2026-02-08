from fastapi import FastAPI

from app.routers.holamundo import router as holamundo_router

app = FastAPI(
    title="control de stock bien",
    version="BETA"
)

app.include_router(holamundo_router, prefix="/holamundo")
