# backend/app/models/product/move/moveDetail.py

from app.database import Base
from app.models.product.product import Product
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Float, ForeignKey, Integer, String
from .move import Move

class MoveDetail(Base):
    __tablename__ = "move_detail"

    id: Mapped[int] = mapped_column(primary_key=True)

    id_move: Mapped[int] = mapped_column(ForeignKey("move.id"))
    id_product: Mapped[int] = mapped_column(ForeignKey("product.id"))

    # snapshot producto
    product_name: Mapped[str] = mapped_column(String)
    bc_product: Mapped[str] = mapped_column(String)
    unit: Mapped[int] = mapped_column(Integer)

    # cantidad
    ammount: Mapped[int]

    # precios
    unit_price: Mapped[float] = mapped_column(Float)          # precio lista
    unit_price_final: Mapped[float] = mapped_column(Float)   # con descuento

    # descuentos
    discount_percent: Mapped[float]
    discount_amount: Mapped[float]

    # totales
    subtotal: Mapped[float] = mapped_column(Float)           # unit_price * ammount
    total_price: Mapped[float] = mapped_column(Float)              # unit_price_final * ammount

    move: Mapped["Move"] = relationship(back_populates="details")
    product: Mapped["Product"] = relationship(back_populates="move_details")
