from data import (
    TAXIS,
    RIDERS,
    RIDES
)

def serialize(items):
    if type(items) is list:
        return [item.to_dict() for item in items]
    else:
        return items.to_dict()

def get_rider(rider_id):
    rider = None

    for rider_it in RIDERS:
        if rider_it.id == rider_id:
            rider = rider_it
            break

    return rider

def get_all_riders():
    return [rider for rider in RIDERS]

def get_rider_rides(rider_id):
    return [ride for ride in RIDES if ride.rider.id == rider_id]

