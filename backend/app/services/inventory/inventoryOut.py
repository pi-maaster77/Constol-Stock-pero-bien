# backend/app/services/inventory/inventoryOut.py

# backend/app/services/inventory/out.py

from typing import TYPE_CHECKING

from app.models import Move
from app.models.product.batch.batch import Batch
from app.models.product.move.moveDetail import MoveDetail
from app.models.product.product import Product
from sqlalchemy.orm import selectinload

from app.schemas.product.move.move import MoveOutRead

if TYPE_CHECKING:
    from sqlalchemy.orm import Session
    from app.services.inventory import InventoryService

from app.schemas.product.move import move as schemas

# TODO: Cambiar los ValueError por una excepcion personalizada

def register_out(self:"InventoryService", products_out: schemas.MovesOut):
    
    move = Move(date=products_out.date, type="out")
    self.db.add(move)
    self.db.flush()

    ticket_total = 0

    for item in products_out.details:

        product = self.db.get(Product, item.id_product)

        if not product:
            raise ValueError("Product not found")

        if product.ammount < item.ammount:
            raise ValueError("Insufficient stock")

        ammount = item.ammount
        unit_price = product.public_price

        # ---------- descuento bulk ----------
        discount_percent = 0

        for d in product.bulk_discounts:
            if ammount >= d.min_ammount:
                discount_percent = d.discount

        discount_amount = unit_price * discount_percent
        final_price = unit_price - discount_amount
        line_total = final_price * ammount

        ticket_total += line_total

        # ---------- FIFO ----------
        remaining = ammount

        batches = (
            self.db.query(Batch)
            .filter(Batch.id_product == product.id, Batch.ammount > 0)
            .order_by(Batch.received_at)
            .with_for_update()
            .all()
        )

        for batch in batches:
            if remaining <= 0:
                break

            take = min(batch.ammount, remaining)
            batch.ammount -= take
            remaining -= take

        if remaining > 0:
            raise ValueError("Stock inconsistency")

        product.ammount -= ammount

        # ---------- snapshot ----------
        detail = MoveDetail(
            id_move=move.id,
            id_product=product.id,
            product_name=product.name,
            bc_product=product.bc,
            unit=product.unit_id,
            ammount=ammount,
            unit_price=unit_price,
            discount_percent=discount_percent,
            discount_amount=discount_amount,
            unit_price_final=final_price,
            subtotal=unit_price * ammount,
            total_price=line_total,
        )

        self.db.add(detail)

    try:
        self.db.commit()    
        self.db.refresh(move)
    except:
        self.db.rollback()
        raise
    
    assert move.date is not None
    response:MoveOutRead = schemas.MoveOutRead(
        id=move.id,
        date=move.date,
        total=ticket_total,
        details=[
            schemas.TicketLine(
                ammount=detail.ammount,
                id_product=detail.id_product,
                product_name=detail.product_name,
                unit_price=detail.unit_price,
                discount=detail.discount_percent,
                line_total=detail.ammount * detail.unit_price
            ) for detail in move.details
        ]
    )


    return response