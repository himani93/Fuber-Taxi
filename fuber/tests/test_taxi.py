import pytest

from ..exceptions import (
    InvalidTaxiLicenseNumberException,
    InvalidTaxiColorException,
)
from ..taxi import Taxi

class TestTaxi(object):

    def setup(self):
        self.yellow_taxi = Taxi("KA-01-HH-1234")
        self.pink_taxi = Taxi("KA-01-PP-1111")

    def test_taxi_invalid_license_no(self):
        with pytest.raises(TypeError) as context:
            Taxi()

        with pytest.raises(InvalidTaxiLicenseNumberException) as context:
            Taxi(None)
        assert "None is not valid" in context.value

        with pytest.raises(InvalidTaxiLicenseNumberException) as context:
            Taxi("")
        assert " is not valid" in context.value


    def test_taxi_invalid_color(self):
        with pytest.raises(InvalidTaxiColorException) as context:
            Taxi("KA-01-HH-1234", None)
        assert "None is not valid" in context.value

        with pytest.raises(InvalidTaxiColorException) as context:
            Taxi("KA-01-HH-1234", "")
        assert " is not valid" in context.value

    def test_taxi(self):
        assert self.yellow_taxi.license_no == "KA-01-HH-1234"
        assert self.yellow_taxi.color == "yellow"

    def test_taxi_category(self):
        pass

    def test_taxi_available(self):
        pass
