from fastapi import FastAPI
from swapi.db import create_db_and_tables, engine
from sqlmodel import Session, select
from swapi.db_populate import populate_empty_tables
from swapi.model import Planet

app = FastAPI()


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
async def list_planets():
    with get_session() as session:
        planets = session.exec(select(Planet)).all()
        return planets
