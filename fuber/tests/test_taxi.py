import pytest

from ..exceptions import (
    InvalidTaxiLicenseNumberException,
    InvalidTaxiColorException,
)
from ..taxi import Taxi

class TestTaxi(object):

    def setup(self):
        self.yellow_taxi = Taxi("KA-01-HH-1234")
        self.pink_taxi = Taxi("KA-01-PP-1111", "pink")
        self.black_taxi = Taxi("KA-01-BB-1237", "black")

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

    def test_taxi_license_no(self):
        assert self.yellow_taxi.license_no == "KA-01-HH-1234"
        with pytest.raises(AttributeError) as context:
            self.yellow_taxi.license_no = "KA-01-01-0101"

    def test_taxi_color(self):
        assert self.yellow_taxi.color == "yellow"
        with pytest.raises(AttributeError) as context:
            self.yellow_taxi.color= "Black"

    def test_taxi_is_available_by_default(self):
        assert self.yellow_taxi.available == True
        self.yellow_taxi.available = False
        assert self.yellow_taxi.available == False

    def test_taxi_category(self):
        assert self.yellow_taxi.category == "default"
        assert self.pink_taxi.category == "pink"
        assert self.black_taxi.category == "default"
        with pytest.raises(AttributeError) as context:
            self.yellow_taxi.category = "sedan"
