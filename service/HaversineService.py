"""

Haversine

"""

from haversine import haversine


def linear_distance(distance):
    return haversine((distance.first_lat_coordinate, distance.first_lon_coordinate), (distance.second_lat_coordinate, distance.second_lon_coordinate))
