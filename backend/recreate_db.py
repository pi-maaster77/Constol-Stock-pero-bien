#!/usr/bin/env python3

from app.database import Base, engine
import os
from dotenv import load_dotenv

load_dotenv()

# Drop all tables
Base.metadata.drop_all(bind=engine)

# Create all tables
Base.metadata.create_all(bind=engine)

print("Database tables recreated successfully.")