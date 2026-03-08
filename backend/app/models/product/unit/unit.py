# backend/app/models/product/unit/unit.py

from typing import List, Optional
from sqlalchemy.orm import Mapped
from datetime import date

from app.database import Base


from sqlalchemy.orm import Mapped, mapped_column, relationship

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.product.product import Product

class Unit(Base):
    __tablename__ = "unit"


    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    abbreviation: Mapped[str]

    products: Mapped[List["Product"]] = relationship(back_populates="unit")
