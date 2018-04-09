import datetime
import pytest

from ..ride import Ride
from ..rider import Rider
from ..location import Location
from ..exceptions import (
    InvalidLocationException,
    InvalidRiderException,
)

class TestRide(object):

    def setup(self):
        self.rider_yami = Rider("Yami")
        self.ride_one = Ride(Location(1, 2), Location(2, 3), self.rider_yami)

    def test_ride_id(self):
       assert type(self.ride_one.id) == str
       assert len(self.ride_one.id) == 36
       with pytest.raises(AttributeError):
            self.ride_one.id = 8

    def test_invalid_pickup_drop_location(self):
        with pytest.raises(InvalidLocationException) as context:
            Ride(1, 2, self.rider_yami)

    def test_ride_location_cannot_be_changed(self):
        ride_two = Ride(Location(1, 2), Location(3, 4), self.rider_yami)
        with pytest.raises(AttributeError) as context:
            ride_two.drop_location = Location(3, 6)
        with pytest.raises(AttributeError) as context:
            ride_two.pickup_location = Location(3, 6)

    def test_ride_invalid_start_end_time(self):
        pass

    def test_invalid_ride_rider(self):
        with pytest.raises(InvalidRiderException) as context:
            Ride(Location(1, 2), Location(2, 5), None)
        with pytest.raises(InvalidRiderException) as context:
            Ride(Location(1, 2), Location(2, 5), "")

    def test_ride_created(self):
        assert type(self.ride_one.pickup_location) == Location
        assert type(self.ride_one.drop_location) == Location
        assert isinstance(self.ride_one.start_time, datetime.datetime) == True
        assert self.ride_one.end_time == None
        assert self.ride_one.status == "processing"
        assert self.ride_one.rider == self.rider_yami

