# backend/app/models/product/price/lifo.py

from sqlalchemy import select
from ..batch.batch import Batch


def lifo_price(session, id_product: int):

    return session.execute(
        select(Batch.cost_price)
        .where(Batch.id_product == id_product)
        .order_by(Batch.received_at.desc())
        .limit(1)
    ).scalar()
