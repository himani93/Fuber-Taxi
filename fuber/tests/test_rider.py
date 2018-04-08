import pytest

from ..rider import Rider
from ..exceptions import InvalidRiderNameException

class TestRider(object):

    def setup(self):
        self.rider_himani = Rider("Himani")

    def test_invalid_rider_name(self):
        with pytest.raises(InvalidRiderNameException) as context:
            Rider(None)
        assert "None is not valid" in context.value

        with pytest.raises(InvalidRiderNameException) as context:
            Rider("")
        assert " is not valid" in context.value

    def test_rider_name(self):
        assert self.rider_himani.name == "Himani"

    def test_rider_id(self):
        assert type(self.rider_himani.id) == str
        assert len(self.rider_himani.id) == 36
        with pytest.raises(AttributeError):
            self.rider_himani.id = 8

    def test_rider_repr(self):
        assert repr(self.rider_himani) == "Rider(Himani - {})".format(self.rider_himani.id)

    def test_rider_str(self):
        assert str(self.rider_himani) == "Himani"
