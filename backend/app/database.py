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

engine = create_engine(DATABASE_URL, echo=DATABASE_ECHO)

Base = declarative_base()

def init_db():
    from sqlalchemy.orm import sessionmaker
    from app.models.product.unit.unit import Unit

    from app.models.product.unit.defaultUnits import default_units

    SessionLocal = sessionmaker(bind=engine)
    db = SessionLocal()

    try:
        for u in default_units:
            exists = db.query(Unit).filter_by(id=u["id"]).first()

            if not exists:
                db.add(Unit(**u))

        db.commit()
        print("Unidades inicializadas.")

    except Exception as e:
        db.rollback()
        print(f"Error al inicializar: {e}")

    finally:
        db.close()


init_db()