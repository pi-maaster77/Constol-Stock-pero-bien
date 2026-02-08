from sqlalchemy import select
from typing import TYPE_CHECKING


from backend.app.models.product.batch.batch import Batch

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