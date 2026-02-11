# backend/app/models/product/discount/discountBulk.py

from sqlalchemy import Float, Integer, UniqueConstraint
from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

class DiscountBulk(Base):
    __tablename__ = "bulk_discount"

    id: Mapped[int] = mapped_column(primary_key=True)

    id_product: Mapped[int] = mapped_column(ForeignKey("product.id"))

    min_ammount: Mapped[int] = mapped_column(Integer)      # umbral
    discount: Mapped[float] = mapped_column(Float)  # 0.10 = 10%

    product = relationship("Product", back_populates="bulk_discounts")

    __table_args__ = (
        UniqueConstraint("id_product", "min_ammount", name="unique_discount_rule"),
    )
