# backend/app/schemas/product/discount.py

from typing import Optional
from pydantic import BaseModel, ConfigDict

class DicountBulkBase(BaseModel):
    id_product: int
    min_ammount: int
    discount: float

class DiscountBulkCreate(DicountBulkBase):
    pass

class DiscountBulkUpdate(BaseModel):
    min_ammount: Optional[int] = None
    discount: Optional[float] = None

class DiscountBulk(DicountBulkBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
