import helper
from .exceptions import (
    InvalidRiderNameException,
    InvalidRidingStatusException,
    RidingStatusSameException,
)


class Rider(object):
    def __init__(self, rider_name):
        if not rider_name:
            raise InvalidRiderNameException("{} is not valid".format(rider_name))

        self._id = helper.get_id()
        self.name = rider_name
        self._riding = False

    def __repr__(self):
        return "Rider({} - {})".format(self.name, self.id)

    def __str__(self):
        return self.name

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "riding": self.riding,
        }

    @property
    def id(self):
        return self._id

    @property
    def riding(self):
        return self._riding

    @riding.setter
    def riding(self, status):
        if type(status) is not bool:
            raise InvalidRidingStatusException("{} is not valid".format(status))

        if status == self._riding:
            raise RidingStatusSameException("Riding status is already {}".format(self.riding))

        self._riding = status
