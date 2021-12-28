"""

Routes here:

- Where am I ?
    - Return the street, city and country a given geolocation point is at.

- Linear distance (Haversine)
    - Return the linear distance on a globe given two geo-coordinates.

"""

from fastapi import APIRouter
from service.HaversineService import linear_distance
from model.linearDistance import linearDistance
from model.pairCoordinate import pairCoordinate
from service.whereAmIService import getLocation
router = APIRouter()


@router.get("/linearDistance")
def get_linear_distance(distance: linearDistance):
    result_in_kilometers = linear_distance(distance)
    return {"Kilometers": result_in_kilometers}


@router.get("/whereAmI")
def get_where_am_i(local: pairCoordinate):
    location = getLocation(local)
    return {"Location": location}
