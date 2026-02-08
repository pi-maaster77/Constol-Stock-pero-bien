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
