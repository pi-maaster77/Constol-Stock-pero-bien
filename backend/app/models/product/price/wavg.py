# backend/app/models/product/price/wavg.py

from sqlalchemy import select, func
from ..batch.batch import Batch


def weighted_avg_price(session, id_product):

    return session.execute(
        select(
            func.sum(Batch.cost_price * Batch.ammount) /
            func.sum(Batch.ammount)
        )
        .where(Batch.id_product == id_product)
    ).scalar()
