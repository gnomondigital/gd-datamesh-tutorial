"""import modules"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from gd_nasa_api.infra.postgres_handler import PostgresHandler


postgres_handler = PostgresHandler()
engine = postgres_handler.launch_connection_db()

Base = declarative_base()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
