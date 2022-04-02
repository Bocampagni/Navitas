import requests


def getLocation(local):
    requestResult = requests.get(f"https://nominatim.openstreetmap.org/reverse?lat={local.lat_coordinate}&lon={local.lon_coordinate}&zoom=10&format=json")
    location = requestResult.json()['display_name']
    return location

