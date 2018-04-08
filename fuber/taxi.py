from exceptions import (
    InvalidTaxiLicenseNumberException,
    InvalidTaxiColorException,
)


class Taxi(object):
    def __init__(self, license_no, color="yellow"):
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

    @property
    def license_no(self):
        return self._license_no

    @property
    def color(self):
        return self._color

    @property
    def category(self):
        return self._category
