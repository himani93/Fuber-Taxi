from collections import defaultdict

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

def get_rider_current_ride(rider_id):
    current_ride = None
    rider_rides = get_rider_rides(rider_id)
    on_going_rides = filter(lambda ride: ride.is_on_going(), rider_rides)

    try:
        current_ride = on_going_rides[0]
    except IndexError:
        pass

    return current_ride

def get_available_taxis():
    return [taxi for taxi in TAXIS if taxi.available]

def get_nearest_available_taxi(pickup_location):
    nearest_taxi = None

    available_taxis = get_available_taxis()
    available_taxis_with_location = filter(lambda taxi: taxi.location is not None, available_taxis)
    taxi_to_pickup_distance = defaultdict(list)

    for taxi in available_taxis_with_location:
        distance = pickup_location.distance(taxi.location)
        taxi_to_pickup_distance[distance].append(taxi)

    if not taxi_to_pickup_distance:
        return nearest_taxi

    shortest_distance = min(taxi_to_pickup_distance.keys())
    nearest_taxis = taxi_to_pickup_distance[shortest_distance]

    try:
        nearest_taxi = nearest_taxis[0]
    except IndexError as e:
        pass

    return nearest_taxi
