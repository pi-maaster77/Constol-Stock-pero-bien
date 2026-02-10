# backend/app/routers/moves.py

from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import engine
from app.models import Product, Move, MoveDetail, Batch
from app.schemas.product.move import move as schemas


router = APIRouter(
    prefix="/moves",
    tags=["moves"],
)

def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()

@router.post("/in", response_model=schemas.MoveInRead)
def products_in(products_in: schemas.MovesIn, db: Session = Depends(get_db)):

    try:
        move = Move(date=products_in.date)
        db.add(move)
        db.flush()

        for item in products_in.details:

            # crear batch
            batch = Batch(
                id_product=item.id_product,
                date=item.date,
                ammount=item.ammount,
                price=item.price
            )
            db.add(batch)

            # registrar detalle del movimiento
            detail = MoveDetail(
                id_move=move.id,
                id_product=item.id_product,
                ammount=item.ammount
            )
            db.add(detail)
            # actualizar stock producto
            product = db.get(Product, item.id_product)
            if product == None:
                raise HTTPException(status_code=404, detail="Product not found")
            product.ammount += item.ammount
        db.commit()
        db.refresh(move)

        from sqlalchemy.orm import selectinload

        move = (
            db.query(Move)
            .filter(Move.id == move.id)
            .options(selectinload(Move.details))
            .first()
        )

        return move

    except:
        db.rollback()
        raise


@router.post("/out", response_model=schemas.MoveOutRead)
def products_out(products_out: schemas.MovesOut, db: Session = Depends(get_db)):

    move = Move(date=products_out.date)
    db.add(move)
    db.flush()

    ticket_total = 0

    for item in products_out.details:

        product = db.get(Product, item.id_product)

        if not product:
            raise HTTPException(404, "Product not found")

        if product.ammount < item.ammount:
            raise HTTPException(400, "Insufficient stock")

        ammount = item.ammount
        unit_price = product.public_price

        # ---------- descuento bulk ----------
        discount_percent = 0

        for d in product.bulk_discounts:
            if ammount >= d.min_qty:
                discount_percent = d.discount

        discount_amount = unit_price * discount_percent
        final_price = unit_price - discount_amount
        line_total = final_price * ammount

        ticket_total += line_total

        # ---------- FIFO ----------
        remaining = ammount

        batches = (
            db.query(Batch)
            .filter(Batch.id_product == product.id, Batch.ammount > 0)
            .order_by(Batch.date)
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
            raise HTTPException(400, "Stock inconsistency")

        product.ammount -= ammount

        # ---------- snapshot ----------
        detail = MoveDetail(
            move_id=move.id,
            product_id=product.id,
            product_name=product.name,
            ammount=ammount,
            unit_price_original=unit_price,
            discount_percent=discount_percent,
            discount_amount=discount_amount,
            unit_price_final=final_price,
            line_total=line_total,
        )

        db.add(detail)

    move.total = ticket_total

    db.commit()
    db.refresh(move)

    return move