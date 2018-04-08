import falcon

from controller.taxi_app import TaxiApp


api = application = falcon.API()
taxi_app = TaxiApp()


api.add_route("/taxis/", taxi_app)
api.add_route("/taxis/{taxi_id}", taxi_app)

# if __name__ == "__main__":
