import datetime
import helper

from rider import Rider
from exceptions import (
    InvalidLocationException,
    InvalidRiderException,
)
from location import Location


class Ride(object):
    def __init__(self, pickup_location, drop_location, rider):
        self._id = helper.get_id()

        if pickup_location is not None and type(pickup_location) is not Location:
            raise InvalidLocationException("{} is not of Location type".format(pickup_location))
        self._pickup_location = pickup_location

        if drop_location is not None and type(drop_location) is not Location:
            raise InvalidLocationException("{} is not of Location type".format(drop_location))
        self._drop_location = drop_location

        if type(rider) is not Rider:
            raise InvalidRiderException("{} is not a valid Rider".format(rider))

        self._rider = rider
        self._start_time = datetime.datetime.now()
        self._end_time = None
        self._status = "started"

    @property
    def id(self):
        return self._id

    @property
    def pickup_location(self):
        return self._pickup_location

    @property
    def drop_location(self):
        return self._drop_location

    @property
    def rider(self):
        return self._rider

    @property
    def start_time(self):
        return self._start_time

    @property
    def end_time(self):
        return self._end_time

    @property
    def status(self):
        return self._status

    def end_ride(self):
        # set end time
        # set status to complete
        # set cost
        # set taxi as available
        # customer riding to False
        pass
