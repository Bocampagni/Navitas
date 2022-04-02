"""

Routes here:

- ShippingPrice
    - Return the price to ship a weightless item from a geo-coordinate to another geo-coordinate in meters.

"""

from fastapi import APIRouter
from src.model.linearDistance import linearDistance
from src.service.shortestPathService import getShortestPath
from src.service import shippingPriceService
shippingRoute = APIRouter()


@shippingRoute.post("/shipping")
def getShippingPrice(distance: linearDistance):
    shortestPathInMeters = getShortestPath(distance)
    return shippingPriceService.getShippingPrice(shortestPathInMeters)
