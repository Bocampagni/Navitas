"""

Get the fuel price from database

"""
from ..repository.mongoConnection import mongoConnection


# Todo Change value from hardcoded to dynamic stored data.
def getShippingPrice(distance):
    fuelPrices = mongoConnection()

    return {
        "car": {
            "gasoline": distance * fuelPrices['gasoline'],
            "ethanol": distance * fuelPrices['ethanol'],
            "gnv": distance * fuelPrices['gnv'],
        },
        "motorcycle": {
            "gasoline": distance * fuelPrices['gasoline']
        }
    }
