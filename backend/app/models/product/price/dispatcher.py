# backend/app/models/product/price/dispatcher.py

from ..product import Product, PriceFormula
from .fifo import fifo_price
from .lifo import lifo_price
from .wavg import weighted_avg_price


def calc_product_price(session, product):

    match product.price_formula:

        case PriceFormula.FIFO:
            return fifo_price(session, product.id)

        case PriceFormula.LIFO:
            return lifo_price(session, product.id)

        case PriceFormula.WAVG:
            return weighted_avg_price(session, product.id)

        case _: 
            raise ValueError("Price formula not found")