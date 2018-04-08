from .exceptions import InvalidRiderNameException


class Rider(object):
    def __init__(self, rider_name):
        if not rider_name:
            raise InvalidRiderNameException("{} is not valid".format(rider_name))

        self.name = rider_name
