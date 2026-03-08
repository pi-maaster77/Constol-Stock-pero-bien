# backend/app/models/product/unit/defaultUnits.py

import enum

default_units = [
    {"id": 1, "name": "Unidad", "abbreviation": "u"},
    {"id": 2, "name": "Gramo", "abbreviation": "g"},
    {"id": 3, "name": "Mililitro", "abbreviation": "ml"},
]


class DefaultUnits(enum.IntEnum):
    UNIT = 1
    GRAM = 2
    ML = 3