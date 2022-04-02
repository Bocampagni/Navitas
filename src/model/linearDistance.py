from pydantic import BaseModel


class linearDistance(BaseModel):
    first_lon_coordinate: float
    first_lat_coordinate: float
    second_lon_coordinate: float
    second_lat_coordinate: float
