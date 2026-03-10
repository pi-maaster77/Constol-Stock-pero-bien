# backend/migrate_db.py

#!/usr/bin/env python3

import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL not set in .env")
if DATABASE_URL.startswith("sqlite:///"):
    db_path = DATABASE_URL[10:]  # remove sqlite:///
else:
    raise ValueError("Not SQLite")

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Add missing columns
cursor.execute("ALTER TABLE move_detail ADD COLUMN bc_product TEXT;")
cursor.execute("ALTER TABLE move_detail ADD COLUMN unit INTEGER;")
cursor.execute("ALTER TABLE move_detail ADD COLUMN total_price REAL;")

# Rename total to total_price if exists, but since it's new, perhaps not needed
# But to be safe, if total exists, copy to total_price
cursor.execute("UPDATE move_detail SET total_price = total WHERE total_price IS NULL;")
cursor.execute("UPDATE move_detail SET bc_product = '' WHERE bc_product IS NULL;")
cursor.execute("UPDATE move_detail SET unit = 1 WHERE unit IS NULL;")

conn.commit()
conn.close()

print("Database updated successfully.")