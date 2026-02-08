from sqlalchemy import select, func
from ..batch.batch import Batch


def weighted_avg_price(session, product_id):

    return session.execute(
        select(
            func.sum(Batch.price * Batch.ammount) /
            func.sum(Batch.ammount)
        )
        .where(Batch.id_product == product_id)
    ).scalar()
