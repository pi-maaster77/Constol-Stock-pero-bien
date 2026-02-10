# backend/app/schemas/product/move/mode_detail.py

# backend/app/schemas/schemas.py
from typing import Optional
from pydantic import BaseModel, ConfigDict
import datetime

from app.models.product.product import PriceFormula
from app.models.product.unit.defaultUnits import DefaultUnits


class ProductSelling(BaseModel):
    id_product: int
    ammount: int



class MoveDetailRead(BaseModel):
    id_product: int
    ammount: int

    model_config = ConfigDict(from_attributes=True)



class TicketLine(BaseModel):
    product_id: int
    product_name: str
    qty: int

    unit_price: float
    discount: float
    line_total: float

    model_config = ConfigDict(from_attributes=True)
