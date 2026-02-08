from sqlalchemy.orm import Mapped
from datetime import date

from app.database import Base, fk
from app.models.product.product import Product


from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base



class Batch(Base):
    __tablename__ = "expire"

    id: Mapped[int] = mapped_column(primary_key=True)

    id_product: Mapped[int] = mapped_column(fk(Product.id))
    date: Mapped[date]
    ammount: Mapped[int]
    price: Mapped[float]

    product: Mapped[Product] = relationship(back_populates="batches")

from typing import List, Optional
from sqlalchemy.orm import Mapped