# backend/app/routers/moves.py

from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import engine
from app.models import Product, Move, MoveDetail, Batch
from app.schemas.product.move import move as schemas

from app.services.inventory import InventoryService


router = APIRouter(
    prefix="/moves",
    tags=["moves"],
)

def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()

@router.post("/in", response_model=schemas.MoveInRead)
def products_in(products_in: schemas.MovesIn, db: Session = Depends(get_db)):
    try:
        return InventoryService(db).register_entry(products_in)
    except ValueError:
        raise
    except:
        raise


@router.post("/out", response_model=schemas.MoveOutRead)
def products_out(products_out: schemas.MovesOut, db: Session = Depends(get_db)):
    try:
        return InventoryService(db).register_exit(products_out)
    except ValueError:
        raise
    except:
        raise
