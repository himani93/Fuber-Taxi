import pytest

from ..location import Location
from ..exceptions import (
    InvalidLocationLatitudeException,
    InvalidLocationLongitudeException,
)


class TestLocation(object):
    def setup(self):
        self.taj_mahal_location = Location(1, 18)

    def test_invalid_latitude(self):
        with pytest.raises(InvalidLocationLatitudeException) as context:
            Location(None, 1)
        with pytest.raises(InvalidLocationLatitudeException) as context:
            Location("", 1)
        with pytest.raises(InvalidLocationLatitudeException) as context:
            Location("a", 1)
        with pytest.raises(InvalidLocationLatitudeException) as context:
            Location("1", 1)

    def test_invalid_longitude(self):
        with pytest.raises(InvalidLocationLongitudeException) as context:
            Location(1, None)
        with pytest.raises(InvalidLocationLongitudeException) as context:
            Location(1, "")
        with pytest.raises(InvalidLocationLongitudeException) as context:
            Location(1, "a")
        with pytest.raises(InvalidLocationLongitudeException) as context:
            Location(1, "1")

    def test_location_repr(self):
        assert repr(self.taj_mahal_location) == "Location(1, 18)"

    def test_location_str(self):
        assert str(self.taj_mahal_location) == "Location(1, 18)"

    def test_location_latitude(self):
        assert self.taj_mahal_location.latitude == 1
        with pytest.raises(AttributeError) as context:
            self.taj_mahal.latitude = 22

    def test_location_longitude(self):
        assert self.taj_mahal_location.longitude == 18
        with pytest.raises(AttributeError) as context:
            self.taj_mahal.longitude = 22

    def test_distance_between_two_locations(self):
        hawa_mahal_location = Location(-2, 1)
        amer_fort_location = Location(1, 5)

        assert hawa_mahal_location.distance(amer_fort_location) == 5
