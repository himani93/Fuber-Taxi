import falcon
import json

from data import TAXIS
from models.taxi import Taxi
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
        return [taxi.to_dict() for taxi in TAXI if taxi.available]

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
            if request_params.get("available", False):
                taxis = self._get_available_taxis()
            else:
                taxis = self._get_all_taxis()

            response.body = json.dumps({"taxis": taxis})
            response.status = falcon.HTTP_200

    def on_post(self, request, response):
        body = json.load(request.stream)
        try:
            taxi = Taxi(body.get("license_no"), body.get("color"))
        except InvalidTaxiColorException as e:
            response.body = json.dumps({"message": "Taxi color is not valid"})
            response.status = falcon.HTTP_400
        except InvalidTaxiLicenseNumberException as e:
            response.body = json.dumps({"message": "Taxi license number is not valid"})
            response.status = falcon.HTTP_400
        else:
            TAXIS.append(taxi)
            response.body = json.dumps({"message": "Taxi registered.", "data": taxi.to_dict()})
            response.status = falcon.HTTP_201
