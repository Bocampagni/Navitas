"""

MongoDb connection

"""

from pymongo import MongoClient


def getMongoConnection():
    client = MongoClient("mongodb://db:27017", username='admin', password='admin')
    return client.shipping.fuelPrices
