from sqlmodel import SQLModel, create_engine

sqllite_file_name = "database.sqlite"
sqlite_url = f"sqlite:///{sqllite_file_name}"


connect_args = {"check_same_thread": False}

engine = create_engine(sqlite_url, connect_args=connect_args, echo=True)


def create_db_and_tables():
    from . import model  # noqa: F401

    SQLModel.metadata.create_all(engine)
