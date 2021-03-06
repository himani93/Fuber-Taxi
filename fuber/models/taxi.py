import helper

from exceptions import (
    InvalidTaxiLicenseNumberException,
    InvalidTaxiColorException,
    InvalidLocationException,
)
from location import Location


class Taxi(object):
    def __init__(self, license_no, color="yellow", location=None):
        if not license_no:
            raise InvalidTaxiLicenseNumberException("{} is not valid".format(license_no))
        self._license_no = license_no

        if not color:
            raise InvalidTaxiColorException("{} is not valid".format(color))
        self._color = color

        if color == "pink":
            self._category = "pink"
        else:
            self._category = "default"

        self.available = True
        self.location = location
        self._id = helper.get_id()

    def __repr__(self):
        return "Taxi({} - {} - {})".format(self.license_no, self.color, self.available)

    def __str__(self):
        return "Taxi({} - {} - {})".format(self.license_no, self.color, self.available)

    def to_dict(self):
        return {
            "id": self.id,
            "license_no": self.license_no,
            "color": self.color,
            "available": self.available,
            "category": self.category,
            "location": self.location.to_dict() if self.location else self.location,
        }

    @property
    def license_no(self):
        return self._license_no

    @property
    def color(self):
        return self._color

    @property
    def category(self):
        return self._category

    @property
    def id(self):
        return self._id

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, loc):
        if loc is not None and type(loc) is not Location:
            raise InvalidLocationException("{} is not of Location type".format(loc))

        self._location = loc

    def is_pink(self):
        return True if self.category == "pink" else False
