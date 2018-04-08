import math

from exceptions import (
    InvalidLocationLatitudeException,
    InvalidLocationLongitudeException,
)


class Location(object):
    def __init__(self, lat, lon):
        if not lat or type(lat) is not int:
            raise InvalidLocationLatitudeException("{} is not valid".format(lat))
        self._latitude = lat

        if not lon or type(lon) is not int:
            raise InvalidLocationLongitudeException("{} is not valid".format(lon))
        self._longitude = lon

    def __repr__(self):
        return "Location({}, {})".format(self._latitude, self._longitude)

    def __str__(self):
        return "Location({}, {})".format(self._latitude, self._longitude)

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

