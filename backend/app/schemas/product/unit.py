# backend/app/schemas/product/unit.py

from typing import Optional
from pydantic import BaseModel, ConfigDict
import datetime

from app.models.product.product import PriceFormula
from app.models.product.unit.defaultUnits import DefaultUnits

class UnitBase(BaseModel):
    
    name: str
    abbreviation: str


class UnitCreate(UnitBase):
    name: str
    abbreviation: str

class UnitPatch(BaseModel):
    id: int
    name: Optional[str] = None
    abbreviation: Optional[str] = None

class UnitReturn(UnitBase):
    id: int
    model_config = ConfigDict(from_attributes=True)