"""

Routes here:

- ShippingPrice
    - Return the price to ship a weightless item from a geo-coordinate to another geo-coordinate in meters.

"""

from fastapi import APIRouter
from model.linearDistance import linearDistance
from service.shortestPathService import getShortestPath
from service.shippingPrice import getShippingPrice
shippingRoute = APIRouter()


@shippingRoute.post("/shipping")
async def getShippingPrice(distance: linearDistance):
    distance_in_kilometers = getShortestPath(distance)
    return getShippingPrice(distance_in_kilometers)
