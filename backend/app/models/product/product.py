from __future__ import annotations

from typing import List, Optional
import enum
from sqlalchemy import (
    Enum,
    Integer,
    String,
    Boolean,
    Float,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.product.batch.batch import Batch
    from app.models.product.move.moveDetail import MoveDetail


class PriceFormula(enum.Enum):
    FIFO = "FIFO"
    LIFO = "LIFO"
    WAVG = "WAVG"



class Product(Base):
    __tablename__ = "product"


    id: Mapped[int] = mapped_column(primary_key=True)
    bc: Mapped[str] = mapped_column(String)
    name: Mapped[str] = mapped_column(String)
    ammount: Mapped[int] = mapped_column(Integer, default=0)
    unit: Mapped[int] = mapped_column(Integer, default=0)
    expire: Mapped[bool] = mapped_column(Boolean, default=False)


    price: Mapped[Optional[float]] = mapped_column(Float)


    price_formula: Mapped[PriceFormula] = mapped_column(
    Enum(PriceFormula, name="price_formula_type"),
    nullable=False
    )


    batches: Mapped[List["Batch"]] = relationship(back_populates="product")
    move_details: Mapped[List["MoveDetail"]] = relationship(back_populates="product")


