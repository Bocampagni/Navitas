"""

Routes here:

- ShippingPrice
    - Return the price to ship a weightless item from a geo-coordinate to another geo-coordinate in meters.

"""

from fastapi import APIRouter
from model.linearDistance import linearDistance
from service.shortestPathService import getShortestPath

shippingRoute = APIRouter()


@shippingRoute.post("/shipping")
async def getShippingPrice(distance: linearDistance):
    distanceInMeters = getShortestPath(distance)
    distanceInKilometers = (distanceInMeters / 1000)
    response = {
        "car": {
            "gasoline": distanceInKilometers * 7,
            "ethanol": distanceInKilometers * 5.9,
            "gnv": distanceInKilometers * 5,
            "diesel": distanceInKilometers * 4
        },
        "motorcycle": {
            "gasoline": distanceInKilometers * 6
        }
    }
    return response
