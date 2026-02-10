# backend/app/models/product/product.py

from __future__ import annotations
from typing import List, Optional
import enum

from sqlalchemy import (
    Enum as SAEnum,
    Integer,
    String,
    Boolean,
    Float,
    ForeignKey,
)

from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.product.batch.batch import Batch
    from app.models.product.move.moveDetail import MoveDetail
    from app.models.product.discount.discountBulk import DiscountBulk
    from app.models.product.unit.unit import Unit

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
    expires: Mapped[bool] = mapped_column(Boolean, default=False)

    price_cache: Mapped[Optional[float]] = mapped_column(Float)

    active: Mapped[bool] = mapped_column(Boolean, default=True)


    price_formula: Mapped[PriceFormula] = mapped_column(
        SAEnum(
            PriceFormula,
            native_enum=False,
            validate_strings=True,
            values_callable=lambda x: [e.value for e in x],
        ),
        nullable=False,
    )

    public_price: Mapped[float] = mapped_column(Float)

    batches: Mapped[List["Batch"]] = relationship(back_populates="product")
    move_details: Mapped[List["MoveDetail"]] = relationship(back_populates="product")
    bulk_discounts: Mapped[List["DiscountBulk"]] = relationship(
        back_populates="product",
        order_by="DiscountBulk.min_qty.asc()"
    )
    unit_id: Mapped[int] = mapped_column(Integer, ForeignKey("unit.id"), nullable=False, default=1)
    unit: Mapped["Unit"] = relationship(back_populates="products")

    
