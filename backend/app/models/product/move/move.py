
from typing import List, Optional
from sqlalchemy.orm import Mapped
from datetime import date

from app.database import Base


from sqlalchemy.orm import Mapped, mapped_column, relationship

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.product.move.moveDetail import MoveDetail

class Move(Base):
    __tablename__ = "move"


    id: Mapped[int] = mapped_column(primary_key=True)
    date: Mapped[Optional[date]]


    details: Mapped[List["MoveDetail"]] = relationship(back_populates="move")