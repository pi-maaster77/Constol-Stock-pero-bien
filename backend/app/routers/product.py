# backend/app/routers/product.py

from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import engine
from app.models import Product
from app.schemas.product import product as schemas


router = APIRouter(
    prefix="/product",
    tags=["product"],
)

def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.ProductReturn)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    db_product = Product(
        bc=product.bc,
        name=product.name,
        price_formula=product.price_formula,
        public_price=product.public_price,
        unit_id=product.unit_id,
        expires=product.expires
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@router.get("/", response_model=List[schemas.ProductReturn])
def read_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    products = db.query(Product).filter(Product.active == True).offset(skip).limit(limit).all()
    return products

@router.get("/{id_product}", response_model=schemas.ProductReturn)
def read_product(id_product: int, db: Session = Depends(get_db)):
    db_product = db.query(Product).filter(Product.id == id_product).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

@router.get("/bc/{bc_product}", response_model=schemas.ProductReturn)
def read_product_by_bc(bc_product: int, db: Session = Depends(get_db)):
    db_product = db.query(Product).filter(Product.bc == bc_product).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

@router.patch("/{id_product}", response_model=schemas.ProductReturn)
def patch_product(
    id_product: int,
    product_patch: schemas.ProductPatch,
    db: Session = Depends(get_db)
):
    db_product = db.query(Product).filter(Product.id == id_product).first()

    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")

    update_data = product_patch.dict(exclude_unset=True)

    for field, value in update_data.items():
        setattr(db_product, field, value)

    db.commit()
    db.refresh(db_product)

    return db_product

@router.delete("/{id_product}", response_model=schemas.ProductReturn)
def delete_product(id_product: int, db: Session = Depends(get_db)):
    db_product = db.query(Product).filter(Product.id == id_product).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    
    db_product.active = False
    
    db.commit()
    db.refresh(db_product)

    return db_product
