# backend/app/database.py

from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.orm import declarative_base
from os import environ as env

import os

if os.getenv("PYTEST_CURRENT_TEST") is None:
    try:
        import dotenv
        dotenv.load_dotenv()
    except ModuleNotFoundError:
        pass

DATABASE_URL = env.get("DATABASE_URL")
DATABASE_ECHO = env.get("DATABASE_ECHO", "").lower() in ("1", "true", "yes")

if DATABASE_URL is None:
    raise TypeError("La URL de la base de datos es nula")


def fk(column):
    return ForeignKey(f"{column.table.name}.{column.key}")


engine = create_engine(DATABASE_URL, echo=DATABASE_ECHO)

Base = declarative_base()

def init_db():
    from sqlalchemy.orm import sessionmaker
    SessionLocal = sessionmaker(bind=engine)
    db = SessionLocal()
    from app.models.product.unit.unit import Unit
    try:
        # Verificar si ya existe el color por defecto (ej. ID 1 o nombre 'Gris')
        default_unit = db.query(Unit).filter_by(id=1).first()
        if not default_unit:
            unit = Unit(id=1, nombre="Unidad", abreviation="u")
            db.add(unit)
            db.commit()
            print("Unidad creada con exito.")
                # Verificar si ya existe el color por defecto (ej. ID 1 o nombre 'Gris')
        default_gram = db.query(Unit).filter_by(id=2).first()
        if not default_gram:
            unit = Unit(id=2, nombre="Gramo", abreviation="g")
            db.add(unit)
            db.commit()
            print("Unidad creada con exito.")
                    # Verificar si ya existe el color por defecto (ej. ID 1 o nombre 'Gris')
        default_mililiter = db.query(Unit).filter_by(id=3).first()
        if not default_mililiter:
            unit = Unit(id=3, nombre="mililitro", abreviation="ml")
            db.add(unit)
            db.commit()
            print("Unidad creada con exito.")
    except Exception as e:
        print(f"Error al inicializar: {e}")
        db.rollback()
    finally:
        db.close()

init_db()