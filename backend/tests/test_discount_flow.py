# backend/tests/test_discount_flow.py

import pytest
from sqlalchemy.orm import Session

from app.models.product.product import Product, PriceFormula
from app.models.product.discount.discountBulk import DiscountBulk
from app.models.product.discount.dispatcher import calculate_discounted_price


def setup_product_with_discounts(session: Session) -> Product:
    """
    Crea un producto con un precio base de 100.0 y dos reglas de descuento:
    - 10% para 5 o más unidades.
    - 20% para 10 o más unidades.
    """
    product = Product(
        name="Producto Con Descuento",
        bc="779-DISC",
        price_formula=PriceFormula.WAVG,  # No es relevante para este test
        public_price=100.0,
    )
    session.add(product)
    session.flush()  # Para obtener el product.id

    # Regla 1: 10% de descuento a partir de 5 unidades
    discount1 = DiscountBulk(id_product=product.id, min_ammount=5, discount=0.10)

    # Regla 2: 20% de descuento a partir de 10 unidades
    discount2 = DiscountBulk(id_product=product.id, min_ammount=10, discount=0.20)

    session.add_all([discount1, discount2])
    session.commit()
    return product


@pytest.mark.parametrize(
    "ammount, expected_total_price",
    [
        (1, 100.0),  # Sin descuento: 1 * 100
        (4, 400.0),  # Sin descuento, justo por debajo del umbral: 4 * 100
        (5, 450.0),  # 10% de descuento: (5 * 100) * (1 - 0.10)
        (9, 810.0),  # 10% de descuento: (9 * 100) * (1 - 0.10)
        (10, 800.0), # 20% de descuento: (10 * 100) * (1 - 0.20)
        (20, 1600.0),# 20% de descuento: (20 * 100) * (1 - 0.20)
    ],
)
def test_calculate_discounted_price_with_rules(
    session: Session, ammount: int, expected_total_price: float
):
    """
    Verifica que el cálculo del precio con descuento funcione correctamente
    para un producto que tiene reglas de descuento.
    """
    # 1. Setup
    product = setup_product_with_discounts(session)

    # 2. Ejecución
    final_price = calculate_discounted_price(
        session=session, id_product=product.id, ammount=ammount
    )

    # 3. Aserción
    assert final_price == pytest.approx(expected_total_price)


def test_calculate_price_for_product_without_discounts(session: Session):
    """
    Verifica que el precio no se altera para un producto sin reglas de descuento.
    """
    # 1. Setup
    product = Product(
        name="Producto Sin Descuento",
        bc="779-NO-DISC",
        price_formula=PriceFormula.FIFO,
        public_price=50.0,
    )
    session.add(product)
    session.commit()

    # 2. Ejecución
    final_price = calculate_discounted_price(
        session=session, id_product=product.id, ammount=10
    )

    # 3. Aserción
    # Precio esperado: 10 unidades * 50.0 cada una = 500.0
    assert final_price == pytest.approx(500.0)

