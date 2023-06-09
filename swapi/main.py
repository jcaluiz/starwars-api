from fastapi import FastAPI, Response
from swapi.db import create_db_and_tables, engine
from sqlmodel import Session, select
from swapi.db_populate import populate_empty_tables
from swapi.model import Planet
import os
from fastapi.middleware.cors import CORSMiddleware
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "data", "database.sqlite")


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
    "https://example.com",
    "https://www.example.com",
    "https://jcaluiz.github.io/Project-StartWars-Planet-Search/",
    "https://jcaluiz.github.io/",
    "http://jcaluiz.github.io/",
    "https://starwars-api-production.up.railway.app",
    "https://starwars-api-production.up.railway.app/get_planets",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_session():
    return Session(engine)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()
    with get_session() as session:
        populate_empty_tables(session)


@app.get("/", tags=["main"])
async def root():
    return {"message": "Hello World!"}


@app.get("/get_planets", tags=["planets"])
async def list_planets(response: Response):
    with get_session() as session:
        planets = session.exec(select(Planet)).all()
        response.headers["Access-Control-Allow-Origin"] = "*"
        return planets
