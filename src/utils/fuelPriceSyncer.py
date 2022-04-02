from src.utils.convertToNumber import getNumberConversion
from src.utils.getFuelList import getFuelList
from src.repository.mongoConnection import getMongoConnection


def getFuelPrice():
    db = getMongoConnection()

    # scrapping fuel prices
    fuel_list = getFuelList()
    fuel_prices = getNumberConversion(fuel_list)

    # Persisting fuel prices
    return db.insert_one({'gasoline': fuel_prices[1], 'ethanol': fuel_prices[0], 'gnv': fuel_prices[2]})
