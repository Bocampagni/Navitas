from pydantic import BaseModel


class pairCoordinate(BaseModel):
    lat_coordinate: float
    lon_coordinate: float
