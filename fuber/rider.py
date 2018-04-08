import helper
from .exceptions import InvalidRiderNameException


class Rider(object):
    def __init__(self, rider_name):
        if not rider_name:
            raise InvalidRiderNameException("{} is not valid".format(rider_name))

        self._id = helper.get_id()
        self.name = rider_name

    def __repr__(self):
        return "Rider({} - {})".format(self.name, self.id)

    def __str__(self):
        return self.name

    @property
    def id(self):
        return self._id
