# backend/app/models/product/discount/discountBulk.py

from sqlalchemy import Float, Integer
from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

class DiscountBulk(Base):
    __tablename__ = "bulk_discount"

    id: Mapped[int] = mapped_column(primary_key=True)

    product_id: Mapped[int] = mapped_column(ForeignKey("product.id"))

    min_qty: Mapped[int] = mapped_column(Integer)      # umbral
    discount_pct: Mapped[float] = mapped_column(Float)  # 0.10 = 10%

    product = relationship("Product", back_populates="bulk_discounts")
