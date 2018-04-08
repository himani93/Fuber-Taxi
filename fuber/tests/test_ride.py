import pytest

from ..ride import Ride


class TestRide(object):

    def setup(self):
        self.ride_one = Ride()

    def test_ride_id(self):
       assert type(self.ride_one.id) == str
       assert len(self.ride_one.id) == 36
       with pytest.raises(AttributeError):
            self.ride_one.id = 8

    def test_invalid_pickup_location(self):
        pass

    def test_invalid_drop_location(self):
        pass

    def test_invalid_ride_start_time(self):
        pass

    def test_invalid_ride_end_time(self):
        pass

    def test_customer(self):
        pass

    def test_taxi(self):
        pass

    def test_ride_status(self):
        pass

    def test_ride_cost(self):
        pass
