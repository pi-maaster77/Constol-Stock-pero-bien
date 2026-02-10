# backend/app/schemas/product/product.py

from typing import Optional
from pydantic import BaseModel, ConfigDict
import datetime

from app.models.product.product import PriceFormula
from app.models.product.unit.defaultUnits import DefaultUnits

class ProductBase(BaseModel):
    bc: str
    name: str
    price_formula: PriceFormula
    public_price: float
    unit_id: DefaultUnits
    expires: bool

class ProductCreate(ProductBase):
    pass

class ProductReturn(ProductBase):
    id: int
    bc: str
    name: str
    ammount: int
    price_cache: Optional[float]
    model_config = ConfigDict(from_attributes=True)

class ProductPatch(BaseModel):
    bc: Optional[str] = None
    name: Optional[str] = None
    price_formula: Optional[PriceFormula] = None
    public_price: Optional[float] = None
    unit_id: Optional[DefaultUnits] = None
    expires: Optional[bool] = None
