import falcon
import json

from data import TAXIS
from models.taxi import Taxi
from models.location import Location
from models.exceptions import *


class TaxiApp(object):
    def _get_taxi(self, taxi_id):
        taxi = None
        for taxi_it in TAXIS:
            if taxi_it.id == taxi_id:
                taxi = taxi_it
                break

        return taxi

    def _get_all_taxis(self):
        return [taxi.to_dict() for taxi in TAXIS]

    def _get_available_taxis(self):
        return [taxi.to_dict() for taxi in TAXIS if taxi.available]

    def _get_pink_available_taxis(self):
        return [taxi.to_dict() for taxi in TAXIS if taxi.is_pink() and taxi.available]

    def on_get(self, request, response, taxi_id=None):
        request_params = request.params

        if taxi_id:
            taxi = self._get_taxi(taxi_id)
            if not taxi:
                raise falcon.HTTPNotFound()
            else:
                response.body = json.dumps(taxi.to_dict())
                response.status = falcon.HTTP_200
        else:
            taxis = []
            if request.get_param_as_bool("available"):
                if request.get_param("category") == "pink":
                    taxis = self._get_pink_available_taxis()
                else:
                    taxis = self._get_available_taxis()
            else:
                taxis = self._get_all_taxis()

            response.body = json.dumps({"taxis": taxis})
            response.status = falcon.HTTP_200

    def on_post(self, request, response):
        body = json.load(request.stream)

        taxi_location = None

        location = body.get("location")
        if location:
            try:
                taxi_location = Location(**location)
            except Exception as e:
                raise falcon.HTTPBadRequest("Taxi Location is invalid")

        try:
            taxi = Taxi(body.get("license_no"), body.get("color"), taxi_location)
        except InvalidTaxiColorException as e:
            raise falcon.HTTPBadRequest("Taxi color is not valid")
        except InvalidTaxiLicenseNumberException as e:
            raise falcon.HTTP.BadRequest("Taxi License number is invalid")

        TAXIS.append(taxi)
        response.body = json.dumps({"message": "Taxi registered.", "data": taxi.to_dict()})
        response.status = falcon.HTTP_201

    def on_patch(self, request, response, taxi_id=None):
        body = json.load(request.stream)

        taxi = self._get_taxi(taxi_id)
        if not taxi:
            raise falcon.HTTPPreconditionFailed

        location = body.get("location")
        try:
            taxi_current_location = Location(location.get("latitude"), location.get("longitude"))
        except (InvalidLocationLatitudeException, InvalidLocationLongitudeException) as e:
            raise falcon.HTTPPreconditionFailed

        taxi.location = taxi_current_location
