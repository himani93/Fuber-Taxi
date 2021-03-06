import datetime
import helper

from rider import Rider
from exceptions import (
    InvalidLocationException,
    InvalidRiderException,
)
from location import Location
from config import Config


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
        self._taxi = None
        self._status = "processing"
        self._fare = None

    def to_dict(self):
        return {
            "pickup_location": self.pickup_location.to_dict() if self.pickup_location else None,
            "drop_location": self.drop_location.to_dict() if self.drop_location else None,
            "rider": self.rider.to_dict(),
            "start_time": str(self.start_time) if self.start_time else None,
            "end_time": str(self.end_time) if self.end_time else None,
            "status": self.status,
            "taxi": self.taxi.to_dict() if self.taxi else None,
            "fare": self.fare if self.fare else 0,
        }

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

    @property
    def taxi(self):
        return self._taxi

    @property
    def fare(self):
        return self._fare

    def _calculate_ride_fare(self):
        cost = 0

        distance = self.pickup_location.distance(self.drop_location)
        time_taken =  (self.end_time - self.start_time).total_seconds() // 60

        cost = distance * Config.PRICE_PER_KM + time_taken * Config.PRICE_PER_MIN
        if self.taxi.is_pink():
            cost += Config.PINK_TAXI_CHARGE

        return cost

    def set_taxi_unavailable(self):
        self._status = "taxi_unavailable"

    def is_on_going(self):
        return True if self.status == "on_going" else False

    def start(self, taxi):
        self._status = "on_going"
        self._taxi = taxi
        self._taxi.available = False
        self._rider.riding = True

    def stop(self):
        self._status = "completed"
        self._end_time = datetime.datetime.now()
        self._taxi.available = True
        self._taxi.location = self.drop_location
        self._rider.riding = False
        self._fare = self._calculate_ride_fare()
