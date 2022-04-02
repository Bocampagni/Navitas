"""

MongoDb connection

"""

from pymongo import MongoClient


def mongoConnection():
    client = MongoClient("mongodb://localhost:27017",username='admin',password='admin')
    return client.fuelPrice