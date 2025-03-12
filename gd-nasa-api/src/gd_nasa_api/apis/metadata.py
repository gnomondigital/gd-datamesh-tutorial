"""import modules"""
import logging

from fastapi import APIRouter
from fastapi.responses import JSONResponse


logger = logging.getLogger(__name__)

router = APIRouter(prefix="")


@router.get("/")
async def healthz():
    message = {"message": "OK"}
    return JSONResponse(content=message, status_code=200)


@router.get("/metadata")
async def get_metadata():
    """
    Summary:
    This code defines a route that returns metadata information about
    the gd-nasa-api.

    """
    message = {
        "name": "gd-nasa-api",
        "description": "Exposing nasa opendata using an api",
    }
    return JSONResponse(content=message, status_code=200)
