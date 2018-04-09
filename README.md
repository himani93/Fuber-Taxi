Assumptions:
---

Assumptions on Taxi:

1. Taxi color is yellow by default.
2. Taxi color cannot change.
3. License number of all taxis are different
4. A taxi is available by default.
5. Taxi location is unkown by default, if so it will not be assigned to any rider

Assumptions on Ride:

1. Ride pickup and drop location are to be provided when starting the ride
2. Start time of ride is when customer booked a ride
3. end of ride id when customer ends the ride
4. Rides end and start time are not same

Assumptions on Price calculation:

1. distance is in KMs
3. Taxi service is available in single timezone
4. only dogecoin works as a currency

#### Fuber Taxi API

[Link to Fuber Taxi API](https://documenter.getpostman.com/view/1597190/fuber-taxi/RVu5iTiX)

#### Postman collection
[Link to Postman Collection](https://www.getpostman.com/collections/1e14735a21e76c5a7e21)


#### Setup:

1. `pip install -r requirements.txt`
2. `pip install -r test_requirements.txt`

#### Start service:

`cd fuber`
`gunicorn app:api --reload --log-file logs.log`
