# backend/app/models/product/price/consume.py

from sqlalchemy import select, func


from app.models.product.batch.batch import Batch

from .dispatcher import calc_product_price


def consume_fifo(session, product_id: int, qty: int):

    batches = session.scalars(
        select(Batch)
        .where(Batch.id_product == product_id)
        .order_by(Batch.date.asc())
    ).all()

    remaining = qty
    total = 0

    for batch in batches:

        if remaining <= 0:
            break

        take = min(batch.ammount, remaining)

        total += take * batch.price

        batch.ammount -= take
        remaining -= take

    if remaining > 0:
        raise Exception("Stock insuficiente")

    return total

def consume_lifo(session, product_id: int, qty: int):

    batches = session.scalars(
        select(Batch)
        .where(Batch.id_product == product_id)
        .order_by(Batch.date.desc())
    ).all()

    remaining = qty
    total = 0

    for batch in batches:

        if remaining <= 0:
            break

        take = min(batch.ammount, remaining)

        total += take * batch.price
        batch.ammount -= take
        remaining -= take

    if remaining > 0:
        raise Exception("Stock insuficiente")

    return total

def consume_wavg(session, product_id: int, qty: int):

    # 1️⃣ calcular promedio ponderado

    avg_price = session.execute(
        select(
            func.sum(Batch.price * Batch.ammount) /
            func.sum(Batch.ammount)
        )
        .where(Batch.id_product == product_id)
    ).scalar()

    if avg_price is None:
        raise Exception("Producto sin stock")

    # 2️⃣ costo total

    total_cost = avg_price * qty

    # 3️⃣ descontar stock físico

    remaining = qty

    batches = session.scalars(
        select(Batch)
        .where(Batch.id_product == product_id)
    ).all()

    for batch in batches:

        if remaining <= 0:
            break

        take = min(batch.ammount, remaining)

        batch.ammount -= take
        remaining -= take

    if remaining > 0:
        raise Exception("Stock insuficiente")

    return total_cost