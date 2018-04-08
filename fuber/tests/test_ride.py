import datetime
import pytest

from ..ride import Ride
from ..location import Location
from ..exceptions import (
    InvalidLocationException,
)

class TestRide(object):

    def setup(self):
        self.ride_one = Ride(Location(1, 2), Location(2, 3))

    def test_ride_id(self):
       assert type(self.ride_one.id) == str
       assert len(self.ride_one.id) == 36
       with pytest.raises(AttributeError):
            self.ride_one.id = 8

    def test_invalid_pickup_drop_location(self):
        with pytest.raises(InvalidLocationException) as context:
            Ride(1,2)

    def test_ride_location_cannot_be_changed(self):
        ride_two = Ride(Location(1, 2), Location(3, 4))
        with pytest.raises(AttributeError) as context:
            ride_two.drop_location = Location(3, 6)
        with pytest.raises(AttributeError) as context:
            ride_two.pickup_location = Location(3, 6)

    def test_ride_invalid_start_end_time(self):
        pass

    def test_ride_created(self):
        assert type(self.ride_one.pickup_location) == Location
        assert type(self.ride_one.drop_location) == Location
        assert isinstance(self.ride_one.start_time, datetime.datetime) == True
        assert self.ride_one.end_time == None

    def test_customer(self):
        pass

    def test_taxi(self):
        pass

    def test_ride_status(self):
        pass

    def test_ride_cost(self):
        pass
