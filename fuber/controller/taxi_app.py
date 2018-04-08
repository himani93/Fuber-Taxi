import falcon
import json

from data import TAXIS
from models.taxi import Taxi
from models.exceptions import *


class TaxiApp(object):
    def _get_taxi(self, taxi_id):
        taxi = None
        for taxi_it in TAXIS:
            if taxi_it.id == tax_id:
                taxi = taxi_it
                break

        return taxi

    def on_get(self, request, response, taxi_id=None):
        if taxi_id:
            taxi = self._get_taxi(taxi_id)
            if not taxi:
                raise falcon.HTTPNotFound()
            else:
                response.body = json.dumps({"id": taxi_id})
                response.status = falcon.HTTP_200
        else:
            response.body = json.dumps({"taxis": TAXIS})
            response.status = falcon.HTTP_200

    def on_post(self, request, response):
        body = json.load(request.stream)
        try:
            taxi = Taxi(body.get("license_no"), body.get("color"))
            print taxi.id
        except InvalidTaxiColorException as e:
            response.body = json.dumps({"message": "Taxi color is not valid"})
            response.status = falcon.HTTP_400
        except InvalidTaxiLicenseNumberException as e:
            response.body = json.dumps({"message": "Taxi license number is not valid"})
            response.status = falcon.HTTP_400
        else:
            TAXIS.append(taxi)
            print TAXIS
            response.body = json.dumps({"message": "Taxi registered."})
            response.status = falcon.HTTP_201
