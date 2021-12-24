"""

Haversine

"""

from haversine import haversine


def linear_distance(local):
    return haversine((local.first_lat_coordinate, local.first_lon_coordinate), (local.second_lat_coordinate, local.second_lon_coordinate))
