import falcon
import json

from data import TAXIS
from fuber.taxi import Taxi


class TaxiApp(object):
    def on_get(self, request, response):
        response.body = json.dumps({"taxis": TAXIS})
        response.status = falcon.HTTP_200

    def on_post(self, request, response):
        body = request.stream.read()
        try:
            taxi = Taxi(body.get("license_no"), body.get("color"))
        except Exception as e:
            print e
            response.status = falcon.HTTP_400
        else:
            TAXIS.append(taxi)
            response.status = falcon.HTTP_201
