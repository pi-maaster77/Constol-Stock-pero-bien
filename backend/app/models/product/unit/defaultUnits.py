# backend/app/models/product/unit/defaultUnits.py

import enum

default_units = [
    {"id": 1, "name": "Unidad", "abreviation": "u"},
    {"id": 2, "name": "Gramo", "abreviation": "g"},
    {"id": 3, "name": "Mililitro", "abreviation": "ml"},
]


class DefaultUnits(enum.IntEnum):
    UNIT = 1
    GRAM = 2
    ML = 3