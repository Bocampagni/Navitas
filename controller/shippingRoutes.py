"""

Routes here:

- ShippingPrice
    - Return the price to ship a weightless item from a geo-coordinate to another geo-coordinate in meters.

"""

from fastapi import APIRouter
from model.linearDistance import linearDistance

shippingRoute = APIRouter()


@shippingRoute.post("/shipping")
async def getShippingPrice(distance: linearDistance):
    return {"message": "2k"}
