#!/usr/bin/env python3

from sqlalchemy.orm import sessionmaker
from app.database import engine
from app.models import Product

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

db = SessionLocal()

# Create a sample product
product = Product(
    bc="12312312412",
    name="pito",
    price_formula="FIFO",
    public_price=15.0,
    unit_id=1,
    expires=False
)

db.add(product)
db.commit()
db.refresh(product)

print(f"Created product: {product.id} - {product.name}")

db.close()