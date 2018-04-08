import pytest

from ..location import Location
from ..exceptions import (
    InvalidLocationLatitudeException,
    InvalidLocationLongitudeException,
)


class TestLocation(object):
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
        taj_mahal_location = Location(1, 18)
        assert repr(taj_mahal_location) == "Location(1, 18)"

    def test_location_str(self):
        taj_mahal_location = Location(1, 18)
        assert str(taj_mahal_location) == "Location(1, 18)"
