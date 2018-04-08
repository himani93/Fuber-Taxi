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
