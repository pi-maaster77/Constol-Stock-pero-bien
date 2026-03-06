# backend/app/services/inventory/__init__.py

from fastapi import Depends
from sqlalchemy.orm import Session
from .inventoryIn import register_in
from .inventoryOut import register_out

from app.database import engine

def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()

class InventoryService:
    def __init__(self, db: Session = Depends(get_db)):
        self.db:Session = db

    register_entry = register_in
    register_exit = register_out