# backend/tests/conftest.py

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import sessionmaker

# Importamos la 'app' y, crucialmente, el 'engine' y 'Base' de la aplicación.
# El 'engine' ya estará configurado para usar la base de datos en memoria
# gracias a la variable de entorno que estableces en tu comando de pytest.
from app.main import app
from app.database import Base, engine

# Esta fixture 'client' es ahora mucho más simple.
@pytest.fixture(scope="function")
def client():
    # 1. Crea todas las tablas definidas en los modelos de SQLAlchemy
    #    usando el motor de la aplicación.
    Base.metadata.create_all(bind=engine)
    
    # 2. Proporciona el cliente de prueba.
    yield TestClient(app)
    
    # 3. Borra todas las tablas después de que la prueba termine.
    #    Esto asegura que cada prueba comience con una base de datos limpia.
    Base.metadata.drop_all(bind=engine)

# Mantenemos una fixture de sesión por si alguna otra prueba la necesita directamente.
@pytest.fixture(scope="function")
def session():
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    
    Base.metadata.create_all(bind=engine)
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)
