# backend/app/models/product/discount/doscount.py

def apply_bulk_discount(product, qty, base_price):

    for rule in reversed(product.bulk_discounts):
        if qty >= rule.min_qty:
            return base_price * (1 - rule.discount_pct)

    return base_price
