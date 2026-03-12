# backend/app/services/inventory/inventoryAdjustment.py

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

def register_adjust(self: "InventoryService", products_adjust: schemas.MovesAdjust):

    try:
        move = Move(
            date=products_adjust.date,
            reason=products_adjust.reason,
            type="adjust"
        )

        self.db.add(move)
        self.db.flush()

        for item in products_adjust.details:

            product = self.db.get(Product, item.id_product)

            if not product:
                raise ValueError("Product not found")

            # para entradas positivas verificamos expiración según corresponda
            if item.ammount > 0:
                if product.expires and not item.expires_at:
                    raise ValueError("This product requires expiration date")

                if not product.expires and item.expires_at:
                    raise ValueError("This product must NOT have expiration date")

                # crear batch solo para entradas
                batch = Batch(
                    id_product=item.id_product,
                    received_at=item.received_at,
                    expires_at=item.expires_at,
                    ammount=item.ammount,
                    cost_price=item.cost_price
                )

                self.db.add(batch)
            else:
                # salidas: no se exige fecha de vencimiento y no generamos batch
                # opcionalmente podríamos validar que expires_at sea None
                if item.expires_at is not None:
                    # ignorar la fecha o lanzar advertencia según política
                    pass

            # detalle del movimiento permanece siempre, con signo en ammount
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

            # actualizar stock
            product.ammount += item.ammount

        self.db.commit()

        move = (
            self.db.query(Move)
            .filter(Move.id == move.id)
            .options(selectinload(Move.details))
            .first()
        )

        return move

    except:
        self.db.rollback()
        raise