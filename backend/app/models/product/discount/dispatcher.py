# backend/app/models/product/discount/dispatcher.py

from sqlalchemy import select
from .discountBulk import DiscountBulk
from app.models.product.product import Product


def get_bulk_discount(session, product_id: int, ammount: int) -> float:
    """
    Devuelve porcentaje (0.0–1.0)
    """

    rules = session.scalars(
        select(DiscountBulk)
        .where(DiscountBulk.product_id == product_id)
        .order_by(DiscountBulk.min_qty.desc())
    ).all()

    for rule in rules:
        if ammount >= rule.min_qty:
            return rule.discount_pct

    return 0.0


def calculate_discounted_price(session, product_id: int, ammount: int) -> float:
    """
    Calcula el precio final para una cantidad de un producto,
    aplicando descuentos por volumen.
    """
    # 1. Obtener el producto.
    product = session.get(Product, product_id)
    if not product:
        raise ValueError(f"Producto con id {product_id} no encontrado.")

    # 2. Usar el precio público como base.
    base_price = product.public_price

    # 3. Obtener el porcentaje de descuento para la cantidad dada.
    discount_pct = get_bulk_discount(session, product_id, ammount)

    # 4. Calcular el precio total sin descuento.
    total_price = base_price * ammount

    # 5. Aplicar el descuento.
    final_price = total_price * (1 - discount_pct)

    return final_price
