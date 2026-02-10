# backend/tests/test_inventory_flow.py

from datetime import date
import pytest
from sqlalchemy.orm import Session

from app import Product, PriceFormula, Batch, Move, MoveDetail
from app.models.product.price.dispatcher import calc_product_price

def setup_inventory(session: Session, formula: PriceFormula):

    product = Product(
        name=f"Arroz {formula.value}",
        bc=f"123-{formula.value}",
        price_formula=formula,
        public_price=200.0
    )

    session.add(product)
    session.flush()

    # compra 1: 10 @100

    batch1 = Batch(
        id_product=product.id,
        ammount=10,
        price=100,
        date=date(2026, 3, 1)
    )

    # compra 2: 10 @150

    batch2 = Batch(
        id_product=product.id,
        ammount=10,
        price=150,
        date=date(2026, 4, 1)
    )

    session.add_all([batch1, batch2])
    session.flush()

    return product, batch1, batch2

@pytest.mark.parametrize(
    "formula,expected_price",
    [
        (PriceFormula.FIFO, 100),
        (PriceFormula.LIFO, 150),
        (PriceFormula.WAVG, 125),
    ]
)
def test_price_formulas(session, formula, expected_price):

    product, batch1, batch2 = setup_inventory(session, formula)

    price = calc_product_price(session, product)

    assert price == expected_price
