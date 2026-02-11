# backend/app/models/product/price/fifo.py

from sqlalchemy import select
from ..batch.batch import Batch


def fifo_price(session, id_product: int):

    return session.execute(
        select(Batch.cost_price)
        .where(Batch.id_product == id_product)
        .order_by(Batch.received_at.asc())
        .limit(1)
    ).scalar()
