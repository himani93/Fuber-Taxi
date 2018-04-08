import pytest

from ..rider import Rider
from ..exceptions import (
    InvalidRiderNameException,
    InvalidRidingStatusException,
    RidingStatusSameException,
)


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

    def test_default_rider_status(self):
        assert self.rider_himani.riding == False

    def test_rider_set_status(self):
        with pytest.raises(InvalidRidingStatusException) as e:
            self.rider_himani.riding = "False"
        with pytest.raises(RidingStatusSameException) as e:
            self.rider_himani.riding = False

        self.rider_himani.riding = True
        assert self.rider_himani.riding == True
