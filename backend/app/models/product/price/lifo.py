from sqlalchemy import select
from ..batch.batch import Batch


def lifo_price(session, product_id: int):

    return session.execute(
        select(Batch.price)
        .where(Batch.id_product == product_id)
        .order_by(Batch.date.desc())
        .limit(1)
    ).scalar()
