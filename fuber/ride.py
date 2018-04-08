import helper

class Ride(object):
    def __init__(self):
        self._id = helper.get_id()

    @property
    def id(self):
        return self._id
