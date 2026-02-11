# backend/app/models/product/price/consume.py

from sqlalchemy import select, func


from app.models.product.batch.batch import Batch

from .dispatcher import calc_product_price


def consume_fifo(session, id_product: int, ammount: int):

    batches = session.scalars(
        select(Batch)
        .where(Batch.id_product == id_product)
        .order_by(Batch.received_at.asc())
    ).all()

    remaining = ammount
    total = 0

    for batch in batches:

        if remaining <= 0:
            break

        take = min(batch.ammount, remaining)

        total += take * batch.cost_price

        batch.ammount -= take
        remaining -= take

    if remaining > 0:
        raise Exception("Stock insuficiente")

    return total

def consume_lifo(session, id_product: int, ammount: int):

    batches = session.scalars(
        select(Batch)
        .where(Batch.id_product == id_product)
        .order_by(Batch.received_at.desc())
    ).all()

    remaining = ammount
    total = 0

    for batch in batches:

        if remaining <= 0:
            break

        take = min(batch.ammount, remaining)

        total += take * batch.cost_price
        batch.ammount -= take
        remaining -= take

    if remaining > 0:
        raise Exception("Stock insuficiente")

    return total

def consume_wavg(session, id_product: int, ammount: int):

    # 1️⃣ calcular promedio ponderado

    avg_price = session.execute(
        select(
            func.sum(Batch.cost_price * Batch.ammount) /
            func.sum(Batch.ammount)
        )
        .where(Batch.id_product == id_product)
    ).scalar()

    if avg_price is None:
        raise Exception("Producto sin stock")

    # 2️⃣ costo total

    total_cost = avg_price * ammount

    # 3️⃣ descontar stock físico

    remaining = ammount

    batches = session.scalars(
        select(Batch)
        .where(Batch.id_product == id_product)
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