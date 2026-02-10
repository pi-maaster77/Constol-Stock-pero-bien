# backend/app/models/product/discount/doscount.py

def apply_bulk_discount(product, ammount, base_price):

    for rule in reversed(product.bulk_discounts):
        if ammount >= rule.min_qty:
            return base_price * (1 - rule.discount_pct)

    return base_price
