# backend/app/main.py

from os import environ as env
from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI

from app.database import engine, Base
from app.routers import product, discount, moves, unit
import app.models.__init__

if env.get("PYTEST_CURRENT_TEST") is None:
    try:
        import dotenv
        dotenv.load_dotenv()
    except ModuleNotFoundError:
        pass

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="control de stock bien",
    version="BETA",
    root_path="/api"
)

CLIENT = env.get("CLIENT_URL") or "http://localhost:5173"

if CLIENT is None:
    print("CLIENT_URL no está definido, se usará http://localhost:5173")
    raise TypeError("La URL del cliente es nula")

origins = [
    CLIENT
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(product.router)
app.include_router(discount.router)
app.include_router(moves.router)
app.include_router(unit.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}