from datetime import date

from sqlalchemy.orm import Session

from app import Product, PriceFormula, Batch, Move, MoveDetail , consume_fifo


def test_full_inventory_flow(session: Session):

    # 1️⃣ crear producto
    product = Product(
        name="Arroz",
        bc="123",
        price_formula=PriceFormula.FIFO
    )

    session.add(product)
    session.flush()

    # 2️⃣ primera compra (10 unidades a 100)

    move_in_1 = Move()
    session.add(move_in_1)
    session.flush()

    session.add(
        MoveDetail(
            id_move=move_in_1.id,
            id_product=product.id,
            ammount=10
        )
    )

    batch1 = Batch(
        id_product=product.id,
        ammount=10,
        price=100,
        date=date(2026, 3, 1)
    )

    session.add(batch1)

    # 3️⃣ vender 6

    cost1 = consume_fifo(session, product.id, 6)

    assert cost1 == 600
    assert batch1.ammount == 4

    # 4️⃣ segunda compra (10 unidades a 150)

    batch2 = Batch(
        id_product=product.id,
        ammount=10,
        price=150,
        date=date(2026, 4, 1)
    )

    session.add(batch2)

    # 5️⃣ vender 6 más (FIFO: 4 a 100 + 2 a 150)

    cost2 = consume_fifo(session, product.id, 6)

    assert cost2 == 4 * 100 + 2 * 150

    # batch1 vacío
    assert batch1.ammount == 0

    # batch2 quedan 8
    assert batch2.ammount == 8

    # 6️⃣ caducan 3 unidades del batch2

    batch2.ammount -= 3

    # 7️⃣ stock final esperado

    total_stock = batch1.ammount + batch2.ammount

    assert total_stock == 5

    session.rollback()
