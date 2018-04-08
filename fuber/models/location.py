import math

from exceptions import (
    InvalidLocationLatitudeException,
    InvalidLocationLongitudeException,
)


class Location(object):
    def __init__(self, latitude, longitude):
        if not latitude or type(latitude) is not int:
            raise InvalidLocationLatitudeException("{} is not valid".format(latitude))
        self._latitude = latitude

        if not longitude or type(longitude) is not int:
            raise InvalidLocationLongitudeException("{} is not valid".format(longitude))
        self._longitude = longitude

    def __repr__(self):
        return "Location({}, {})".format(self._latitude, self._longitude)

    def __str__(self):
        return "Location({}, {})".format(self._latitude, self._longitude)

    def __eq__(self, other):
        if self.latitude == other.latitude and self.longitude == other.longitude:
            return True
        else:
            return False

    def to_dict(self):
        return {
            "latitude": self.latitude,
            "longitude": self.longitude,
        }

    @property
    def latitude(self):
        return self._latitude

    @property
    def longitude(self):
        return self._longitude

    def distance(self, from_location):
        lat_len = from_location.latitude - self.latitude
        lon_len = from_location.longitude - self.longitude

        distance = math.sqrt(lat_len**2 + lon_len**2)
        return distance
