import pytest

from ..exceptions import (
    InvalidTaxiLicenseNumberException,
    InvalidTaxiColorException,
    InvalidLocationException,
)
from ..taxi import Taxi
from ..location import Location


class TestTaxi(object):

    def setup(self):
        self.yellow_taxi = Taxi("KA-01-HH-1234")
        self.pink_taxi = Taxi("KA-01-PP-1111", "pink")
        self.black_taxi = Taxi("KA-01-BB-1237", "black")

    def test_taxi_id(self):
        assert type(self.yellow_taxi.id) == str
        assert len(self.yellow_taxi.id) == 36
        with pytest.raises(AttributeError):
            self.yellow_taxi.id = 8

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

    def test_taxi_location(self):
        assert self.yellow_taxi.location == None
        with pytest.raises(InvalidLocationException) as context:
            red_taxi = Taxi("KA-09-67-9908", location="")
        with pytest.raises(InvalidLocationException) as context:
            red_taxi = Taxi("KA-09-67-9908", location="A")
        with pytest.raises(InvalidLocationException) as context:
            red_taxi = Taxi("KA-09-67-9908", location=1)

        red_taxi = Taxi("KA-09-67-9908", location=Location(1, 1))
        assert red_taxi.location == Location(1, 1)

        with pytest.raises(InvalidLocationException) as context:
            self.yellow_taxi.location = ""
        with pytest.raises(InvalidLocationException) as context:
            self.yellow_taxi.location = "A"
        with pytest.raises(InvalidLocationException) as context:
            self.yellow_taxi.location = 1

        self.yellow_taxi.location = Location(1, 3)
        self.yellow_taxi.location = None
        self.yellow_taxi = 1

    def test_taxi_repr_str(self):
        assert repr(self.yellow_taxi) == "Taxi(KA-01-HH-1234 - yellow - True)"
        assert repr(self.yellow_taxi) == "Taxi(KA-01-HH-1234 - yellow - True)"
