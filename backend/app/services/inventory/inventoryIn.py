# backend/app/services/inventory/inventoryIn.py

from typing import TYPE_CHECKING

from app.models import Move
from app.models.product.batch.batch import Batch
from app.models.product.move.moveDetail import MoveDetail
from app.models.product.product import Product
from sqlalchemy.orm import selectinload

if TYPE_CHECKING:
    from sqlalchemy.orm import Session
    from app.services.inventory import InventoryService
    from app.schemas.product.move import move as schemas

# TODO: Cambiar los ValueError por una excepcion personalizada

def register_in(self:"InventoryService", products_in: schemas.MovesIn):
    try:
        move = Move(date=products_in.date, type="in")
        self.db.add(move)
        self.db.flush()

        for item in products_in.details:
            product = self.db.get(Product, item.id_product)

            if not product:
                raise ValueError("Product not found")
            assert move is not None
            if product.expires and not item.expires_at:
                raise ValueError("This product requires expiration date")
            if not product.expires and item.expires_at:
                raise ValueError("This product must NOT have expiration date")

            # crear batch
            batch = Batch(
                id_product=item.id_product,
                received_at=item.received_at,
                expires_at=item.expires_at,
                ammount=item.ammount,
                cost_price=item.cost_price
            )
            self.db.add(batch)
            # registrar detalle del movimiento
            detail = MoveDetail(
                id_move=move.id,
                id_product=item.id_product,
                ammount=item.ammount,
                product_name=product.name,
                bc_product=product.bc,
                unit=product.unit_id,
                unit_price=item.cost_price,
                unit_price_final=item.cost_price,
                discount_percent=0,
                discount_amount=0,
                subtotal=item.cost_price * item.ammount,
                total_price=item.cost_price * item.ammount
            )
            self.db.add(detail)
            # actualizar stock producto
            product = self.db.get(Product, item.id_product)
            if product == None:
                raise ValueError("Product not found")
            product.ammount += item.ammount

            move = (
                self.db.query(Move)
                .filter(Move.id == move.id)
                .options(selectinload(Move.details))
                .first()
            )
        self.db.commit()
        self.db.refresh(move)
        return move

    except:
        self.db.rollback()
        raise
