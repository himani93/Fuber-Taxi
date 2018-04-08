import falcon
import json

from models.ride import Ride
from models.location import Location
from models.exceptions import *

import helpers
from data import (
    TAXIS,
    RIDES,
    RIDERS,
)



class RideApp(object):
    def on_get(self, request, response, rider_id=None):
        request_params = request.params

        if ride_id:
            ride = self._get_ride(ride_id)
            if not ride:
                raise falcon.HTTPNotFound()
            else:
                response.body = json.dumps(ride.to_dict())
                response.status = falcon.HTTP_200
        else:
            rides = []
            if request.get_param_as_bool("available"):
                if request.get_param("category") == "pink":
                    rides = self._get_pink_available_rides()
                else:
                    rides = self._get_available_rides()
            else:
                rides = self._get_all_rides()

            response.body = json.dumps({"rides": rides})
            response.status = falcon.HTTP_200

    def on_post(self, request, response, rider_id=None):
        # from pudb import set_trace; set_trace()
        if not rider_id:
            raise falcon.HTTPPreconditionFailed("Rider id not provided")

        rider = helpers.get_rider(rider_id)
        if not rider:
            raise falcon.HTTPPreconditionFailed("Rider with id: {} not found".format(rider_id))

        if rider.riding:
            raise falcon.HTTPUnprocessableEntity("Rider is already riding")

        body = json.load(request.stream)
        pickup_location = body.get("pickup_location")
        drop_location = body.get("drop_location")

        if not pickup_location or not drop_location:
            raise falcon.HTTPPreconditionFailed("Pickup or Drop location not specified")

        try:
            ride = Ride(Location(**pickup_location), Location(**drop_location), rider)
        except Exception as e:
            print e
            raise falcon.HTTPUnprocessableEntity(e)

        taxi = helpers.get_nearest_available_taxi(Location(**pickup_location))
        if not taxi:
            ride.set_taxi_unavailable()
            raise falcon.HTTPUnprocessableEntity("Taxi is unavailable")

        ride.start(taxi)
        RIDES.append(ride)
        response.body = json.dumps({"message": "Ride registered.", "data": ride.to_dict()})
        response.status = falcon.HTTP_201
