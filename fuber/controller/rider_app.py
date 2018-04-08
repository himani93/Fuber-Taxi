import falcon
import json

from data import RIDERS
from models.rider import Rider
from models.exceptions import *


class RiderApp(object):
    def _get_rider(self, rider_id):
        rider = None

        for rider_it in RIDERS:
            if rider_it.id == rider_id:
                rider = rider_it
                break

        return rider

    def _get_all_riders(self):
        return [rider.to_dict() for rider in RIDERS]

    def on_get(self, request, response, rider_id=None):
        if rider_id:
            rider = self._get_rider(rider_id)
            if not rider:
                raise falcon.HTTPNotFound()

            response.body = json.dumps(rider.to_dict())
            response.status = falcon.HTTP_200
        else:
            riders = self._get_all_riders()

            response.body = json.dumps({"riders": riders})
            response.status = falcon.HTTP_200

    def on_post(self, request, response):
        # from pudb import set_trace; set_trace()
        body = json.load(request.stream)
        try:
            rider = Rider(body.get("name"))
        except InvalidRiderNameException as e:
            response.body = json.dumps({"message": "Rider name is not valid"})
            raise falcon.HTTPPreconditionFailed
        else:
            RIDERS.append(rider)
            response.body = json.dumps({"message": "Rider registered.", "data": rider.to_dict()})
            response.status = falcon.HTTP_201

        print rider.id
