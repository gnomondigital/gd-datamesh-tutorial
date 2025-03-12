"""import modules"""
import uvicorn
from fastapi import FastAPI
from sqlalchemy import MetaData

from gd_nasa_api.apis.metadata import router as metadata
from gd_nasa_api.apis.PowerData import router as weatherData
from gd_nasa_api.infra.config import open_data_config
from gd_nasa_api.infra.postgres_handler import PostgresHandler
from gd_nasa_api.infra.powerData import PowerData


postgres_handler = PostgresHandler()

app = FastAPI()
metadata_sql = MetaData()


app.include_router(metadata, tags=["Metadata"])
app.include_router(weatherData, tags=["WeatherData"])


@app.on_event("startup")
def startup_event():
    config = open_data_config()
    engine = postgres_handler.launch_connection_db(
        database_name=config["db_name"]
    )
    PowerData.__table__.create(bind=engine, checkfirst=True)


def run():
    """run for api"""
    uvicorn.run(app, host="0.0.0.0", port=8080)
