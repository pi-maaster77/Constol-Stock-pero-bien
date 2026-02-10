# backend/app/schemas.py

from pydantic import BaseModel, ConfigDict
from app.models.product.product import PriceFormula
from typing import Optional

class ProductBase(BaseModel):
    bc: str
    name: str
    ammount: int = 0
    unit: int = 0
    expire: bool = False
    price_cache: Optional[float] = None
    price_formula: PriceFormula
    public_price: float

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass

class Product(ProductBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class DiscountBulkBase(BaseModel):
    product_id: int
    min_qty: int
    discount_pct: float

class DiscountBulkCreate(DiscountBulkBase):
    pass

class DiscountBulkUpdate(DiscountBulkBase):
    pass

class DiscountBulk(DiscountBulkBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
