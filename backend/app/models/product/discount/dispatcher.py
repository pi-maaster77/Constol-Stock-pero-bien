# backend/app/models/product/discount/dispatcher.py

from sqlalchemy import select
from .discountBulk import DiscountBulk
from app.models.product.product import Product


def get_bulk_discount(session, id_product: int, ammount: int) -> float:
    """
    Devuelve porcentaje (0.0–1.0)
    """

    rules = session.scalars(
        select(DiscountBulk)
        .where(DiscountBulk.id_product == id_product)
        .order_by(DiscountBulk.min_ammount.desc())
    ).all()

    for rule in rules:
        if ammount >= rule.min_ammount:
            return rule.discount

    return 0.0


def calculate_discounted_price(session, id_product: int, ammount: int) -> float:
    """
    Calcula el precio final para una cantidad de un producto,
    aplicando descuentos por volumen.
    """
    # 1. Obtener el producto.
    product = session.get(Product, id_product)
    if not product:
        raise ValueError(f"Producto con id {id_product} no encontrado.")

    # 2. Usar el precio público como base.
    base_price = product.public_price

    # 3. Obtener el porcentaje de descuento para la cantidad dada.
    discount = get_bulk_discount(session, id_product, ammount)

    # 4. Calcular el precio total sin descuento.
    total_price = base_price * ammount

    # 5. Aplicar el descuento.
    final_price = total_price * (1 - discount)

    return final_price
