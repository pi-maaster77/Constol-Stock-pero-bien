# backend/app/schemas/product/barch.py

from pydantic import BaseModel, ConfigDict
import datetime

class BatchCreate(BaseModel):
    id_product: int
    date: datetime.date
    ammount: int
    price: float