"""import modules"""
import logging

from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from gd_nasa_api.infra.session import get_db
from gd_nasa_api.services.dataService import MeteoService


logger = logging.getLogger(__name__)

router = APIRouter(prefix="")
meteo_service = MeteoService()


@router.get("/powerData/countries/{country_name}")
async def country_power_data(country_name: str, db: Session = Depends(get_db)):
    db_power = meteo_service.get_power_data_by_country(
        db=db, country_name=country_name)
    logger.info("db_power: %s", db_power)
    if db_power is None:
        message = {
            "detail": "Engine not found",
        }
        return JSONResponse(content=jsonable_encoder(message), status_code=404)
    return JSONResponse(content=jsonable_encoder(db_power), status_code=200)


@router.get("/powerData/cities/{city_name}")
async def city_power_data(city_name: str, db: Session = Depends(get_db)):
    db_power = meteo_service.get_power_data_by_city(
        db=db, city_name=city_name)
    logger.info("db_power: %s", db_power)
    if db_power is None:
        message = {
            "detail": "Data not found",
        }
        return JSONResponse(content=jsonable_encoder(message), status_code=404)
    return JSONResponse(content=jsonable_encoder(db_power), status_code=200)
