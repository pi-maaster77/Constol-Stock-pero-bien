# backend/app/models/product/move/moveDetail.py

from app.database import Base, fk
from app.models.product.product import Product
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .move import Move

class MoveDetail(Base):
    __tablename__ = "move_detail"


    id: Mapped[int] = mapped_column(primary_key=True)


    id_move: Mapped[int] = mapped_column(fk(Move.id))
    id_product: Mapped[int] = mapped_column(fk(Product.id))


    ammount: Mapped[int]


    move: Mapped[Move] = relationship(back_populates="details")
    product: Mapped[Product] = relationship(back_populates="move_details")