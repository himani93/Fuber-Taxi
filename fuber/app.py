import falcon

from controller.taxi_app import TaxiApp
from controller.rider_app import RiderApp
from controller.ride_app import RideApp

api = application = falcon.API()
taxi_app = TaxiApp()
rider_app = RiderApp()
ride_app = RideApp()

api.add_route("/taxis/", taxi_app)
api.add_route("/taxis/{taxi_id}", taxi_app)

api.add_route("/riders/", rider_app)
api.add_route("/riders/{rider_id}", rider_app)

api.add_route("/riders/{rider_id}/rides", ride_app)

# api.add_route("/riders/{rider_id}/rides/current", ride_app)

