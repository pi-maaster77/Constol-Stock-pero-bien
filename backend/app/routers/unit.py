# backend/app/routers/unit.py

from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import engine
from app.models import Unit
from app.schemas.product import unit as schemas


router = APIRouter(
    prefix="/unit",
    tags=["units"],
)

def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.UnitReturn)
def create_unit(unit: schemas.UnitCreate, db: Session = Depends(get_db)):
    db_unit = Unit(
        name=unit.name,
        abbreviation=unit.abbreviation
    )
    db.add(db_unit)
    db.commit()
    db.refresh(db_unit)
    return db_unit

@router.get("/", response_model=List[schemas.UnitReturn])
def read_units(skip: int = 0, limit: int = 100, db:
    Session = Depends(get_db)):
    units = db.query(Unit).filter(Unit.active == True).offset(skip).limit(limit).all()
    return units

@router.get("/{id_unit}", response_model=schemas.UnitReturn)
def read_unit(id_unit: int, db: Session = Depends(get_db)):
    db_unit = db.query(Unit).filter(Unit.id == id_unit).first()
    if db_unit is None:
        raise HTTPException(status_code=404, detail="Unit not found")
    return db_unit

@router.patch("/{id_unit}", response_model=schemas.UnitReturn)
def patch_unit(
    id_unit: int,
    unit_patch: schemas.UnitPatch,
    db: Session = Depends(get_db)
):
    db_unit = db.query(Unit).filter(Unit.id == id_unit).first()

    if not db_unit:
        raise HTTPException(status_code=404, detail="Unit not found")
    
    if unit_patch.name is not None:
        db_unit.name = unit_patch.name
    if unit_patch.abbreviation is not None:
        db_unit.abbreviation = unit_patch.abbreviation
    db.commit()
    db.refresh(db_unit)
    return db_unit