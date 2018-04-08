import pytest

from ..rider import Rider
from ..exceptions import InvalidRiderNameException

class TestRider(object):

    def test_invalid_rider_name(self):
        with pytest.raises(InvalidRiderNameException) as context:
            Rider(None)
        assert "None is not valid" in context.value

        with pytest.raises(InvalidRiderNameException) as context:
            Rider("")
        assert " is not valid" in context.value

    def test_rider_name(self):
        assert Rider("Himani").name == "Himani"

    def test_rider_id(self):
        rider_himani = Rider("Himani")
        assert type(rider_himani.id) == str
        assert len(rider_himani.id) == 36
        with pytest.raises(AttributeError):
            rider_himani.id = 8
