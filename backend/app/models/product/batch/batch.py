# backend/app/models/product/batch/batch.py

from datetime import date

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from app.database import Base
from app.models.product.product import Product


class Batch(Base):
    __tablename__ = "batch"

    id: Mapped[int] = mapped_column(primary_key=True)

    id_product: Mapped[int] = mapped_column(ForeignKey("product.id"))
    date: Mapped[date]
    ammount: Mapped[int]
    price: Mapped[float]

    product: Mapped["Product"] = relationship(back_populates="batches")