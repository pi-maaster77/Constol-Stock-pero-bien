# backend/tools/create_schema.py

from sqlalchemy.schema import CreateTable
from sqlalchemy.dialects import postgresql
from app.database import Base
from app.models import *

NAME = "Pasar la db a sql"

dialect = postgresql.dialect()

def main():
    for table in Base.metadata.sorted_tables:
        with open("output.sql", "a") as f:
            f.write(str(CreateTable(table).compile(dialect=dialect)) + "\n")