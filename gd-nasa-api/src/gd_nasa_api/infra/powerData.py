from sqlalchemy import Column, Float, Integer, Text
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class PowerData(Base):
    __tablename__ = "s3_power_data_final"
    __table_args__ = {"schema": "gold_opendata"}
    id = Column(Integer, primary_key=True, autoincrement=True)
    lon_x = Column(Float, primary_key=False)
    lat_x = Column(Float, primary_key=False)
    time = Column(Float, primary_key=False)
    ts = Column(Float, primary_key=False)
    ts__max = Column(Float, primary_key=False)
    ts__min = Column(Float, primary_key=False)
    t2_m = Column(Float, primary_key=False)
    t2_m__range = Column(Float, primary_key=False)
    t10_m__range = Column(Float, primary_key=False)
    dist = Column(Float, primary_key=False)
    city = Column(Text, primary_key=False)
    admin_name = Column(Text, primary_key=False)
    lat_y = Column(Float, primary_key=False)
    lon_y = Column(Float, primary_key=False)
    country = Column(Text, primary_key=False)
    capital = Column(Text, primary_key=False)
