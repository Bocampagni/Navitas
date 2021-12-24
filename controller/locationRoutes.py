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

router = APIRouter()


@router.get("/linearDistance")
def get_linear_distance(local: linearDistance):
    result_in_kilometers = linear_distance(local)
    return {"message": result_in_kilometers}
