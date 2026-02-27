# backend/app/main.py

from fastapi import FastAPI

from app.database import engine, Base
from app.routers import product, discount, moves
import app.models.__init__

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="control de stock bien",
    version="BETA",
    openapi_prefix="/api"
)

app.include_router(product.router)
app.include_router(discount.router)
app.include_router(moves.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}