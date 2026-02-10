# backend/app/routers/discount.py
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.product import discount as schemas
from app.database import engine
from app.models.product.discount import discountBulk

router = APIRouter(
    prefix="/discount_bulk",
    tags=["discount_bulk"],
)

def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.DiscountBulk)
def create_discount_bulk(discount: schemas.DiscountBulkCreate, db: Session = Depends(get_db)):
    db_discount = discountBulk.DiscountBulk(**discount.dict())
    db.add(db_discount)
    db.commit()
    db.refresh(db_discount)
    return db_discount

@router.get("/", response_model=List[schemas.DiscountBulk])
def read_discount_bulks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    discounts = db.query(discountBulk.DiscountBulk).offset(skip).limit(limit).all()
    return discounts

@router.get("/{discount_id}", response_model=schemas.DiscountBulk)
def read_discount_bulk(discount_id: int, db: Session = Depends(get_db)):
    db_discount = db.query(discountBulk.DiscountBulk).filter(discountBulk.DiscountBulk.id == discount_id).first()
    if db_discount is None:
        raise HTTPException(status_code=404, detail="Discount not found")
    return db_discount

@router.put("/{discount_id}", response_model=schemas.DiscountBulk)
def update_discount_bulk(discount_id: int, discount: schemas.DiscountBulkUpdate, db: Session = Depends(get_db)):
    db_discount = db.query(discountBulk.DiscountBulk).filter(discountBulk.DiscountBulk.id == discount_id).first()
    if db_discount is None:
        raise HTTPException(status_code=404, detail="Discount not found")
    
    for var, value in vars(discount).items():
        setattr(db_discount, var, value) if value else None

    db.commit()
    db.refresh(db_discount)
    return db_discount

@router.delete("/{discount_id}", response_model=schemas.DiscountBulk)
def delete_discount_bulk(discount_id: int, db: Session = Depends(get_db)):
    db_discount = db.query(discountBulk.DiscountBulk).filter(discountBulk.DiscountBulk.id == discount_id).first()
    if db_discount is None:
        raise HTTPException(status_code=404, detail="Discount not found")
    
    db.delete(db_discount)
    db.commit()
    return db_discount
