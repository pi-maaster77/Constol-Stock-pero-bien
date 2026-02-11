# backend/app/schemas/product/batch.py

from typing import Optional
from pydantic import BaseModel, ConfigDict
from datetime import date 

class BatchCreate(BaseModel):
    id_product: int
    received_at: date
    expires_at: Optional[date]
    ammount: int
    cost_price: float
