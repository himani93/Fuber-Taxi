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
