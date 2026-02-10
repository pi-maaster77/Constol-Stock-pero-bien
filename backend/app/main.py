# backend/app/main.py

from fastapi import FastAPI

from app.database import engine, Base
from app.models.product.product import Product
from app.models.product.batch.batch import Batch
from app.models.product.discount.discountBulk import DiscountBulk
from app.models.product.move.move import Move
from app.models.product.move.moveDetail import MoveDetail
from app.routers import product, discount

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="control de stock bien",
    version="BETA"
)

app.include_router(product.router)
app.include_router(discount.router)
