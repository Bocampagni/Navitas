"""

Get the fuel price from database

"""
from src.repository.mongoConnection import getMongoConnection


def getShippingPrice(distance):
    fuelTable = getMongoConnection()
    fuelPrices = fuelTable.find_one()
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
