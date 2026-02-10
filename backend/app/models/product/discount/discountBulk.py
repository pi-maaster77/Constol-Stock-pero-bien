# backend/app/models/product/discount/discountBulk.py

from typing import TYPE_CHECKING

from sqlalchemy import Float, Integer
from app.database import Base, fk
from sqlalchemy.orm import Mapped, mapped_column, relationship


from app.models.product.product import Product


class DiscountBulk(Base):
    __tablename__ = "bulk_discount"

    id: Mapped[int] = mapped_column(primary_key=True)

    product_id: Mapped[int] = mapped_column(fk(Product.id))

    min_qty: Mapped[int] = mapped_column(Integer)      # umbral
    discount_pct: Mapped[float] = mapped_column(Float)  # 0.10 = 10%

    product = relationship("Product", back_populates="bulk_discounts")
