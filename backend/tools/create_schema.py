# backend/create_schema.py

from sqlalchemy.schema import CreateTable
from sqlalchemy.dialects import postgresql
from app.database import Base
from app.models import *

dialect = postgresql.dialect()

for table in Base.metadata.sorted_tables:
    with open("output.sql", "a") as f:
        f.write(str(CreateTable(table).compile(dialect=dialect)) + "\n")
