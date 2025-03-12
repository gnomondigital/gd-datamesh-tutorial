from pydantic import BaseModel


class PowerDataAnswerSchema(BaseModel):
    lon_x: float
    lat_x: float
    time: str
    ts: float
    ts__max: float
    ts__min: float
    t2_m: float
    t2_m__range: float
    t10_m__range: float
    dist: float
    city: str
    admin_name: str
    lat_y: float
    lon_y: float
    country: str
    capital: str
