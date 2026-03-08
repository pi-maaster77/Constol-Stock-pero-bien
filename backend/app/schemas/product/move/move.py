# backend/app/schemas/product/move/move.py


from typing import Optional
from pydantic import BaseModel, ConfigDict
import datetime

from app.models.product.product import PriceFormula
from app.models.product.unit.defaultUnits import DefaultUnits

from .mode_detail import MoveDetailRead, ProductSelling, TicketLine
from ..batch import BatchCreate


class MovesIn(BaseModel):
    date: datetime.date
    details: list[BatchCreate]

class MovesOut(BaseModel):
    date: datetime.date
    details: list[ProductSelling]
    model_config = ConfigDict(from_attributes=True)

class MoveInRead(BaseModel):
    id: int
    date: datetime.date
    details: list[MoveDetailRead]

    model_config = ConfigDict(from_attributes=True)

class MoveOutRead(BaseModel):
    id: int
    date: datetime.date
    total: float
    details: list[TicketLine]

    model_config = ConfigDict(from_attributes=True)

class MovesAdjust(BaseModel):
    reason: Optional[str] = None
    date: datetime.date
    details: list[BatchCreate]

class MoveAdjustRead(BaseModel):
    id: int
    date: datetime.date
    details: list[MoveDetailRead]

    model_config = ConfigDict(from_attributes=True)

class MoveRead(BaseModel):
    id: int
    date: datetime.date
    type: str
    details: list[MoveDetailRead]

    model_config = ConfigDict(from_attributes=True) 