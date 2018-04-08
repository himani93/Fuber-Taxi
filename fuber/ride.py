import helper

from exceptions import InvalidLocationException
from location import Location


class Ride(object):
    def __init__(self, pickup_location, drop_location):
        self._id = helper.get_id()

        if pickup_location is not None and type(pickup_location) is not Location:
            raise InvalidLocationException("{} is not of Location type".format(pickup_location))
        self._pickup_location = pickup_location

        if drop_location is not None and type(drop_location) is not Location:
            raise InvalidLocationException("{} is not of Location type".format(drop_location))
        self._drop_location = drop_location

    @property
    def id(self):
        return self._id

    @property
    def pickup_location(self):
        return self._pickup_location

    @property
    def drop_location(self):
        return self._drop_location
