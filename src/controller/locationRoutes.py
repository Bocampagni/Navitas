"""

Routes here:

- Where am I ?
    - Return the street, city and country a given geolocation point is at.

- Linear distance (Haversine)
    - Return the linear distance on a globe given two geo-coordinates.

"""

from fastapi import APIRouter
from src.service.HaversineService import linear_distance
from src.model.linearDistance import linearDistance
from src.model.pairCoordinate import pairCoordinate
from src.service.whereAmIService import getLocation
router = APIRouter()


@router.post("/linearDistance")
def get_linear_distance(distance: linearDistance):
    result_in_kilometers = linear_distance(distance)
    return {"Kilometers": result_in_kilometers}


@router.post("/whereAmI")
def get_where_am_i(local: pairCoordinate):
    location = getLocation(local)
    return {"Location": location}
